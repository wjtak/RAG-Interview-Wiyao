# Evaluation Rubric

We score the exercise across six dimensions. The exercise is time-boxed to
**2–3 hours**, so we weight *pragmatism and communication* as heavily as raw
implementation. A small, working, well-explained system beats a large,
half-finished one.

| # | Dimension | What we look for | Weight |
|---|-----------|------------------|:------:|
| 1 | **Works end to end** | We can open the chatbot (URL or a few local commands) and ask questions that get grounded, correct answers. | 25% |
| 2 | **Retrieval quality** | Sensible chunking, embeddings, and top-k retrieval. Answers are actually grounded in the retrieved context. | 20% |
| 3 | **Handles the unknown** | The bot declines / says "not in my knowledge base" for out-of-scope questions instead of hallucinating. | 15% |
| 4 | **Code clarity** | Readable, reasonably structured code. Easy to follow the ingest → retrieve → generate → serve flow. | 15% |
| 5 | **Pragmatism & scoping** | Good time trade-offs. Cut the right corners, documented what was cut and why. | 15% |
| 6 | **Communication** | Clear `NOTES.md`: approach, choices, trade-offs, what you'd do with more time. | 10% |

## What earns bonus points (all optional)

- Source **citations** shown next to answers.
- A minimal **evaluation** of answer quality (even a handful of test Q&A pairs).
- Deployed on **GCP** (Cloud Run / App Engine / Vertex AI).
- Containerized with a working `Dockerfile`.
- Streaming responses / clean chat UX.
- Sensible handling of **prompt injection** or unsafe questions.

## What we explicitly do NOT expect

- Production hardening (autoscaling, custom domains, SSO).
- A large or fancy front-end — a single chat page is enough.
- Fine-tuning or training a model.
- Perfect test coverage.
- Spending more than 3 hours. **Please don't.**

## Red flags

- Answers that confidently invent facts not in the knowledge base.
- No way for us to actually run or see it working.
- No explanation of choices.
- Silently going far over the time limit.
