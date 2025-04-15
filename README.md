# Text-to-SQL Generator

In this project, I fine-tuned an open-source LLaMA 3 model *(Llama-3.2-1B-Instruct*) to translate natural language queries into SQL statements using the *gretelai/synthetic_text_to_sql* dataset. The model is deployed with a simple Gradio UI, accessible via Hugging Face Spaces.

## 

## 🛠️ How it works

1. **Dataset**: gretelai/synthetic_text_to_sql – synthetic text-SQL pairs.
2. **Model**: Fine-tuned Meta's LLaMA 3 using Hugging Face Transformers.
3. **Training**: Done in Google Colab + A100 (notebook provided).
4. **Interface**: Gradio-powered UI for real-time user input and SQL generation.
5. **Deployment**: Hosted on Hugging Face Spaces for public use.

## 🚀  Demo

Try it here 👉 [Hugging Face Space Link
](https://huggingface.co/spaces/ferdaous/texttosqlmodel)
