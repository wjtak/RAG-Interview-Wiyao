# AI Partners — Company Knowledge Base

> **Note for candidates:** This document is the single source of truth for your
> RAG chatbot. All content is fictionalized for the purpose of this interview.
> Your chatbot should answer questions using *only* the information below and
> should decline to answer questions it does not cover.

---

## 1. Company Overview

**AI Partners** (legal name: *We Are AI Partners Ltd.*) is an applied artificial
intelligence consultancy that helps mid-market and enterprise organizations
adopt Generative AI safely and profitably. Founded in **2021**, the company is
headquartered in **Dubai, United Arab Emirates**, with a delivery hub in
**Lisbon, Portugal** and remote team members across EMEA.

Our tagline is *"From AI ambition to AI in production."* We are vendor-neutral:
we recommend the model, cloud, and tools that fit the client's problem rather
than reselling a single platform.

- **Founded:** 2021
- **Headquarters:** Dubai, UAE
- **Secondary hub:** Lisbon, Portugal
- **Team size:** ~45 people (2025)
- **Website:** www.weareaipartners.com
- **General contact:** hello@weareaipartners.com

### Mission

To make advanced AI practical, trustworthy, and measurable for organizations
that don't have a large in-house research team.

### Values

1. **Outcomes over hype** — every engagement is tied to a measurable business KPI.
2. **Ship, then scale** — we prove value with a pilot before large investment.
3. **Responsible by default** — privacy, security, and evaluation are built in,
   not bolted on.
4. **Teach as we build** — we upskill client teams so they own the solution.

---

## 2. Services

AI Partners offers four core service lines.

### 2.1 AI Strategy & Roadmapping

A short (2–4 week) advisory engagement that identifies high-ROI AI use cases,
assesses data readiness, and produces a prioritized roadmap with cost estimates.
Deliverables include a use-case portfolio, a build-vs-buy analysis, and a
governance recommendation.

### 2.2 Generative AI & RAG Systems

Design and build of production Generative AI applications: retrieval-augmented
generation (RAG) chatbots, document intelligence, semantic search, agents, and
copilots. This is our most requested service line. Typical stack choices include
vector databases (pgvector, Qdrant, Vertex AI Vector Search), orchestration
frameworks (LangChain, LlamaIndex), and foundation models from OpenAI,
Anthropic, Google, or open-weight models when data residency requires it.

### 2.3 Machine Learning Engineering & MLOps

Classic ML and MLOps work: forecasting, recommendation, computer vision,
churn/propensity models, plus the pipelines to train, deploy, monitor, and retrain
them. We set up CI/CD for models, feature stores, and drift monitoring.

### 2.4 AI Enablement & Training

Workshops, hands-on bootcamps, and "AI champion" programs that upskill client
teams. Formats range from a half-day executive briefing to a multi-week
engineering enablement track.

---

## 3. Engagement Models

AI Partners works under three commercial models. Clients frequently start with a
Discovery Sprint and graduate to a fixed-scope or retainer engagement.

### 3.1 Discovery Sprint (fixed price)

- **Duration:** 2–4 weeks
- **Goal:** validate feasibility and define scope
- **Output:** technical proof-of-concept + roadmap + estimate
- **Typical price:** USD 15,000–35,000

### 3.2 Fixed-Scope Project (milestone-based)

- **Duration:** 6–16 weeks
- **Goal:** deliver a defined solution to production
- **Billing:** fixed price against milestones
- **Typical price:** USD 60,000–250,000 depending on complexity

### 3.3 Embedded Team / Retainer (time & materials)

- **Duration:** 3+ months, rolling
- **Goal:** ongoing build and operation alongside the client's team
- **Billing:** monthly retainer for a dedicated pod (e.g. 1 lead + 2 engineers)
- **Typical price:** from USD 25,000/month

All prices are indicative and scoped per engagement. We do not charge for the
initial discovery call.

---

## 4. Technology & Platforms

AI Partners is cloud- and model-agnostic but has deep expertise in the following.

- **Clouds:** Google Cloud Platform (preferred and most common in our delivery),
  AWS, and Microsoft Azure.
- **Compute/serving:** Cloud Run, GKE, Vertex AI, AWS SageMaker, Lambda.
- **Foundation models:** OpenAI (GPT family), Anthropic (Claude), Google
  (Gemini / Vertex AI), Mistral, and open-weight models (Llama, Qwen) for
  on-prem or data-residency-sensitive work.
- **Vector stores:** pgvector, Qdrant, Chroma, Vertex AI Vector Search, FAISS.
- **Orchestration:** LangChain, LlamaIndex, and custom lightweight pipelines.
- **Data/eval:** dbt, BigQuery, Ragas and custom evaluation harnesses for
  measuring retrieval and answer quality.

Our default recommendation for a containerized Generative AI service is
**Google Cloud Run** for its simplicity, scale-to-zero pricing, and fast
deployments.

---

## 5. Industries We Serve

AI Partners has delivered projects across:

- **Financial services** — document intelligence for KYC, compliance Q&A
  assistants, fraud-signal enrichment.
- **Healthcare & life sciences** — clinical document search, medical coding
  assistants (with human-in-the-loop review).
- **Retail & e-commerce** — product recommendation, semantic product search,
  customer-support copilots.
- **Real estate** — listing generation, tenant support chatbots, contract
  summarization.
- **Public sector** — multilingual citizen-service assistants.

We do **not** take on projects involving autonomous weapons, mass surveillance
of private individuals, or unlicensed medical diagnosis.

---

## 6. Selected Case Studies

### 6.1 GulfBank — Compliance Knowledge Assistant

A regional bank needed its compliance officers to query thousands of pages of
regulatory circulars. AI Partners built a RAG assistant on Vertex AI with a
pgvector store and human-verifiable citations. Result: average research time per
query dropped from ~25 minutes to under 2 minutes, with a measured 94% answer
accuracy on the evaluation set.

### 6.2 NovaRetail — Support Copilot

An e-commerce retailer deployed a customer-support copilot that drafts replies
grounded in policy and order data. Deployed on Cloud Run. Result: first-response
time reduced by 40% and agent handling time reduced by 28% in the first quarter.

### 6.3 MedArchive — Clinical Document Search

A healthcare provider needed semantic search across de-identified clinical notes.
AI Partners built an on-prem, open-weight solution to satisfy data-residency
rules. All outputs route through a clinician for review before use.

---

## 7. Responsible AI, Data & Security

AI Partners treats privacy, security, and evaluation as core deliverables.

### 7.1 Data handling

- Client data is processed under a signed Data Processing Agreement (DPA).
- We prefer to work within the **client's own cloud tenancy** so data never
  leaves their environment.
- We support data residency requirements (EU, UAE, on-prem) using open-weight
  models where a hosted API is not permitted.
- We do **not** use client data to train third-party foundation models, and we
  disable data-retention/training on provider APIs where that option exists.

### 7.2 Security

- All engineers follow least-privilege access; secrets are stored in a managed
  secret manager (e.g. Google Secret Manager), never in code.
- We run dependency and container scanning in CI.
- Production systems are deployed with audit logging enabled.

### 7.3 Evaluation & guardrails

- Every RAG system ships with an **evaluation harness** measuring retrieval
  precision/recall and answer faithfulness (grounding).
- Systems are prompted and tested to **refuse or defer** when the answer is not
  in the retrieved context, to reduce hallucination.
- High-stakes use cases (health, finance, legal) always include a
  **human-in-the-loop** review step.

---

## 8. The Team & Careers

AI Partners is a compact, senior team: AI engineers, data engineers, ML
engineers, and a small design and delivery group. Most engineers work full-stack
across data, model, and deployment.

### Roles we hire for

- **AI / GenAI Engineer** — builds RAG systems, agents, and evaluation harnesses.
- **ML Engineer** — classic ML and MLOps.
- **Data Engineer** — pipelines, warehousing, feature stores.
- **AI Delivery Lead** — client-facing technical project leadership.

### How we work

- Remote-first with quarterly in-person gatherings.
- Small pods (2–4 people) per client engagement.
- We use AI coding assistants day to day and expect engineers to be fluent with
  them.
- Interview process: intro call → **technical exercise (this RAG task)** →
  technical deep-dive → final conversation with a founder.

To apply, email **careers@weareaipartners.com** with a short note and your work.

---

## 9. Frequently Asked Questions

**Q: Which cloud do you recommend?**
A: We are cloud-agnostic, but our default and most common choice is Google Cloud
Platform, using Cloud Run for containerized services and Vertex AI for managed
models. We also deliver on AWS and Azure.

**Q: Do you resell a specific AI product?**
A: No. We are vendor-neutral and recommend the model, cloud, and tools that best
fit the client's problem and constraints.

**Q: How do you prevent the chatbot from making things up?**
A: We ground answers in retrieved context, instruct and test the model to defer
when information is missing, ship an evaluation harness for faithfulness, and add
human review for high-stakes use cases.

**Q: Will our data be used to train AI models?**
A: No. We disable training/retention on provider APIs where possible and prefer
to run inside your own cloud tenancy or on open-weight models for sensitive data.

**Q: How quickly can we see something working?**
A: A Discovery Sprint (2–4 weeks) typically produces a working proof-of-concept.

**Q: Do you offer training for our own team?**
A: Yes — through our AI Enablement & Training service line, from executive
briefings to multi-week engineering bootcamps.

**Q: What is the smallest way to start working with you?**
A: A free discovery call, followed by a fixed-price Discovery Sprint.

---

## 10. Contact

- **General enquiries:** hello@weareaipartners.com
- **New business / partnerships:** partnerships@weareaipartners.com
- **Careers:** careers@weareaipartners.com
- **Website:** www.weareaipartners.com
- **Headquarters:** Dubai, United Arab Emirates

*Business hours: Sunday–Thursday, 09:00–18:00 GST (Gulf Standard Time).*
