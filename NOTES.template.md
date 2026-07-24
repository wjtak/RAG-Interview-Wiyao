# NOTES — Wiyao TAKOUGNADI
## Time spent

- Total: **~3 hours** : 1H for coding + 1H for deployment + 1H for documentation

The application follows a streamlined, containerized RAG pattern engineered for enterprise reliability, high performance, and clean UI transparency.

- **Ingestion & Indexation:** Document parsing via `TextLoader` and intelligent block segmentation using `RecursiveCharacterTextSplitter` (Chunk size: 500, Overlap: 50).
- **Embeddings & Vector Store:** Powered by Google's `gemini-embedding-2` stored in an in-memory `FAISS` index for zero-latency dense vector retrieval.
- **LLM Engine:** Google's `gemini-3.6-flash` configured with a low temperature (`temperature=0.1`) to prioritize deterministic factual extraction over creative variance.
- **Pipeline Execution & Resilience:** Explicit prompt construction ensures full control over system instructions without opaque framework wrapper overhead. Furthermore, the streaming response parser dynamically handles both string and list object returns, adapting robustly to the latest Gemini 3.x API structural updates.
- **Source Transparency & Smart Filtering:** The retrieval engine queries the top 3 relevant chunks to construct the LLM context, but streamlines user experience by displaying **only the primary source (Chunk 1)** inside a conditional expander. If a fallback is triggered, source displays are suppressed to prevent user confusion.
- **Deployment:** Dockerized and orchestrated via GCP Cloud Run.

## Anti-Hallucination Measures
- Hard-coded fallback directives ("I don't know / that's not in my knowledge base") strictly enforced in the system prompt.
- Dynamic UI gating ensuring source expanders only render when the model successfully answers from the retrieved context.
  
## What I cut for time / would do next

- no fine-tuning or training a model or optimization of chunk size, top k, etc...
- next steps : evaluate the answers, use other llm (hugginface for example) to compare and eventually optimize chunk size, top k, etc...


## How to run it


# clone, install, set env, run
- Clone or fork the repository.
- Log in to https://console.cloud.google.com, At the top left, click on the project selector drop-down and click New Project (or select an existing one). Name it appropriately (e.g., ai-partners-rag).
- In the search bar at the very top of the console, type Cloud Run, then Click on the Cloud Run service.
- On the Cloud Run dashboard, click the button at the top: + Create Service.
- Choose the first option: Deploy a new revision from a source repository.
- Click the Set up with Cloud Build button then for Repository Provider: Select GitHub.
- Authenticate Google Cloud to access your GitHub account, then select your repository and branch (dev or main).
- Build Type: Choose Dockerfile (Cloud Run will automatically detect your Dockerfile at the root).
- Click Save.
- Service Name: Leave as is or modify (e.g., ai-partners-rag).
- Region: Choose a region close to your target users, for example, europe-west1 (Belgium) or europe-west9 (Paris).
- Authentication: Select Allow unauthenticated invocations so your Streamlit app can be accessed publicly via a web URL.
- Environment Variables: expand the Variables & Secrets section and Click + Add variable.
- Name: GOOGLE_API_KEY
- Value: Paste your actual Google Gemini API key get from https://aistudio.google.com
- Click the Create button at the bottom of the page.
- Google Cloud will automatically start building your Docker image in the cloud following your Dockerfile instructions. You can watch the build logs live on your screen.
- Once the deployment finishes (usually takes 1 to 2 minutes), Cloud Run will display a public URL at the top of the page (e.g., [https://ai-partners-rag-xxxx-ew.a.run.app](https://ai-partners-rag-xxxx-ew.a.run.app)).
- Click that URL: your Streamlit application will open in your browser, powered by gemini-3.6-flash, featuring your clean interface and smart Chunk 1 source rendering!


## Known limitations
- Simple model (gemini-3.6-flash)
- free api, token limitation :)
