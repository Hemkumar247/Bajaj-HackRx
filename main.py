import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langflow.load import run_flow_from_json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Define the path to your Langflow JSON file
FLOW_PATH = "Bajaj HackRx.json"

class ChatInput(BaseModel):
    message: str

class ChatOutput(BaseModel):
    response: str

@app.post("/chat", response_model=ChatOutput)
async def chat(chat_input: ChatInput):
    try:
        result = run_flow_from_json(flow=FLOW_PATH, input_value=chat_input.message)
        
        # The result is a list of RunOutputs, let's get the text from the first one
        response = result[0].outputs[0].results.get("text")

        return ChatOutput(response=response)

    except Exception as e:
        print(f"Error running flow: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
