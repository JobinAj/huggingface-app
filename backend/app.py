from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load the Hugging Face model (modify as needed)
model = pipeline("text-generation", model="gpt2")

# Define request body format
class InputText(BaseModel):
    text: str

@app.post("/generate")
def generate_text(input_text: InputText):
    output = model(input_text.text, max_length=50)
    return {"generated_text": output[0]["generated_text"]}
