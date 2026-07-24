import os
import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# Chargement sécurisé des variables
load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# --- 1. INGESTION & INDEXATION ---
@st.cache_resource
def build_vector_store():
    loader = TextLoader("data/ai-partners-knowledge-base.md")
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)
    
    # Utilisation du modèle d'embedding Google de dernière génération
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-2",
        google_api_key=GOOGLE_API_KEY
    )
    
    return FAISS.from_documents(splits, embeddings)

# --- 2. INTERFACE UTILISATEUR & RAG EXPLICITE ---
st.set_page_config(page_title="AI Partners Chat", page_icon="🤖")
st.title("AI Partners Knowledge Bot 🤖")

vector_store = build_vector_store()

# Utilisation du modèle de génération le plus récent et abouti
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash", 
    temperature=0.1, 
    google_api_key=GOOGLE_API_KEY
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        # Réaffichage de la source principale dans l'historique si elle existe
        if "main_source" in msg and msg["main_source"]:
            with st.expander("📚 Voir la source principale"):
                st.write(msg["main_source"][:(500] + "...")

if user_input := st.chat_input("Ex: What engagement models does AI Partners offer?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # --- PIPELINE RAG MANUEL ---
        retrieved_docs = vector_store.similarity_search(user_input, k=3)
        context_text = "\n\n".join([doc.page_content for doc in retrieved_docs])
        
        system_prompt = f"""You are an official assistant for AI Partners.
Use ONLY the following retrieved context to answer the user's question.
If the answer cannot be found in the context, strictly reply with: 'I don't know / that's not in my knowledge base.'
Do not hallucinate.

Context:
{context_text}"""
        
        messages = [
            ("system", system_prompt),
            ("human", user_input)
        ]
        
        # --- LECTURE ROBUSTE DU STREAMING ---
        for chunk in llm.stream(messages):
            if isinstance(chunk.content, list):
                for block in chunk.content:
                    if isinstance(block, dict) and "text" in block:
                        full_response += block["text"]
                    elif isinstance(block, str):
                        full_response += block
            elif chunk.content:
                full_response += str(chunk.content)
                
            message_placeholder.markdown(full_response + "▌")
            
        message_placeholder.markdown(full_response)
        
        # --- FILTRAGE ET AFFICHAGE DE LA SOURCE PRINCIPALE ---
        is_fallback = "I don't know" in full_response
        main_source_text = ""

        if not is_fallback and retrieved_docs:
            # On ne récupère que le premier chunk (la source la plus proche mathématiquement)
            main_source_text = retrieved_docs[0].page_content
            with st.expander("📚 Voir la source principale"):
                st.write(main_source_text[:500] + "...")
        else:
            st.caption("ℹ️ *Aucune source pertinente n'a été utilisée pour cette réponse.*")

    # Sauvegarde dans l'historique avec la source principale unique
    st.session_state.messages.append({
        "role": "assistant", 
        "content": full_response,
        "main_source": main_source_text
    })
