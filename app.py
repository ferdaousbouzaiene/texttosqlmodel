import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
model_path='ferdaous/mytexttosqlmodel3'
model = AutoModelForCausalLM.from_pretrained(
    model_path,  # after you push to HF
    torch_dtype=torch.float16,
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(model_path)


def generate_sql(prompt):
    formatted_prompt = f"### Instruction:\n{prompt}\n\n### SQL:\n"
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=128,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        do_sample=False,
    )
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if "### SQL:" in decoded:
        decoded = decoded.split("### SQL:")[1].strip()
    if "### Explanation:" in decoded:
        decoded = decoded.split("### Explanation:")[0].strip()
    return decoded

gr.Interface(fn=generate_sql,
             inputs=gr.Textbox(lines=4, label="Natural Language SQL Prompt"),
             outputs=gr.Textbox(label="Generated SQL"),
             title="LLaMA-3 SQL Generator",
             description="Enter a natural language question and get a SQL query in return!").launch()
