# AI Partners — Technical Interview: RAG Chatbot

Welcome, and thank you for taking the time to interview with **AI Partners**.

This is a **time-boxed, hands-on exercise**. The goal is not a production-grade
system — it is to see how you reason about a real-world Generative AI task,
make pragmatic trade-offs under time pressure, and ship something that works
end to end.

---

## 🎯 The Objective

Build a **Retrieval-Augmented Generation (RAG) chatbot** over the knowledge base
we provide, and **deploy it behind a simple web front-end** so we can talk to it.

In short:

> Ingest our document → build a retrieval pipeline → wire it to an LLM →
> expose it through a minimal chat UI → deploy it somewhere we can open in a browser.

The knowledge base is here: **[`data/ai-partners-knowledge-base.md`](data/ai-partners-knowledge-base.md)**

It contains information about our (fictionalized) company. A successful chatbot
can answer questions like:

- *"What engagement models does AI Partners offer?"*
- *"How does AI Partners handle client data and privacy?"*
- *"Which industries have you delivered projects in?"*
- *"Who do I contact about a partnership?"*

…and should **gracefully say it doesn't know** when a question is not covered by
the document (no hallucinating).

---

## ⏱️ Time Limit

**2 to 3 hours.** This is a hard cap — please do not spend more.

We would rather see a **small, working, well-explained** system than a large
unfinished one. If you run out of time, stop and document what you *would* have
done next in your `NOTES.md`. Scoping is part of what we evaluate.

Track your time honestly and tell us roughly how long each part took.

---

## ☁️ Deployment

**Our preference is Google Cloud Platform (GCP)** — e.g. Cloud Run, App Engine,
or a Compute Engine VM. GCP experience is a plus for this role.

**But use whatever you can ship fastest.** Any of these are perfectly acceptable:

- **GCP** (preferred) — Cloud Run is a great fit for a containerized app
- Other clouds — AWS (App Runner / Lambda / ECS), Azure Container Apps
- PaaS — Vercel, Render, Railway, Fly.io, Hugging Face Spaces, Streamlit Cloud
- **A local deployment is acceptable** if you cannot deploy remotely — in that
  case, include a **short screen recording or GIF** of it working, plus clear
  run instructions.

The deployment does **not** need a custom domain, HTTPS hardening, or autoscaling.
It needs to be reachable and to work.

---

## 🧰 What You Can Use

- **Any language / framework.** Python (LangChain, LlamaIndex, or plain) and a
  simple front-end (Streamlit, Gradio, a small React/Next app, or plain HTML/JS)
  are all common and fine.
- **Any LLM provider.** OpenAI, Anthropic (Claude), Google (Gemini/Vertex AI),
  Mistral, or a local/open model. Use your own API key — see
  [`.env.example`](.env.example).
- **Any vector store.** FAISS, Chroma, Qdrant, pgvector, or even in-memory — the
  corpus is small, so keep it simple.
- **AI coding assistants are allowed and encouraged** (that's how we work). We
  care about the result and your understanding of it, not whether you typed
  every character.

---

## ✅ What "Done" Looks Like

1. A running chatbot we can open in a browser (URL) **or** run locally in a few
   commands.
2. It answers questions grounded in the provided knowledge base.
3. It cites or references where an answer came from (nice to have, not required).
4. It says "I don't know / that's not in my knowledge base" for out-of-scope
   questions.
5. A clear `README`/`NOTES.md` explaining your approach, choices, and trade-offs.

---

## 📦 What to Submit

See **[`SUBMISSION.md`](SUBMISSION.md)** for the checklist. In short: a link to
your repo, the deployment URL (or recording), and your notes.

---

## 📊 How We Evaluate

See **[`EVALUATION.md`](EVALUATION.md)** for the full rubric. We look at
correctness, retrieval quality, code clarity, pragmatism/scoping, and how well
you communicate your decisions.

---

## 🚀 Suggested Starting Point

A minimal, fast path (feel free to ignore):

1. **Ingest** — load `data/ai-partners-knowledge-base.md`, split into chunks
   (e.g. ~500–1000 tokens with overlap).
2. **Embed & index** — embed chunks, store in FAISS/Chroma (in-memory is fine).
3. **Retrieve** — top-k similarity search on the user's question.
4. **Generate** — prompt the LLM with retrieved context + question, instruct it
   to answer *only* from context and to admit when it doesn't know.
5. **Serve** — wrap it in Streamlit/Gradio or a small API + chat page.
6. **Deploy** — containerize and push to Cloud Run (or your platform of choice).

Good luck — we're excited to see what you build. 🙌

*Questions during the exercise? Email* **mohamed@weareaipartners.com**.
