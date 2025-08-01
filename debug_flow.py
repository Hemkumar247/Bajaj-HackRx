# debug_flow.py
import os
from langflow.load.load import run_flow_from_json
from dotenv import load_dotenv

# --- Your Action Here ---
# Put a simple question you would ask your bot.
test_input = "What is the main purpose of this document?"
# ------------------------

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
astradb_token = os.getenv("ASTRADB_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define tweaks to inject credentials and user_id directly into the flow components
tweaks = {
    # Astra DB components
    "AstraDB-fRR57": {
        "token": astradb_token
    },
    "AstraDB-cC6vF": {
        "token": astradb_token
    },
    # OpenAI Embeddings components
    "OpenAIEmbeddings-YThOJ": {
        "openai_api_key": openai_api_key,
        "model_kwargs": {
            "user": "debug-user"
        }
    },
    "OpenAIEmbeddings-TLefa": {
        "openai_api_key": openai_api_key,
        "model_kwargs": {
            "user": "debug-user"
        }
    },
    # Language Model component
    "LanguageModelComponent-IZklD": {
        "api_key": openai_api_key
    }
}

print("--- Starting Debug Script ---")

# 2. Check if Bajaj HackRx.json exists
if not os.path.exists("Bajaj HackRx.json"):
    print("❌ FATAL: Bajaj HackRx.json file not found in this directory.")
else:
    print("✅ Bajaj HackRx.json found.")
    
    try:
        # 3. Run the flow
        print(f"\nAttempting to run flow with input: '{test_input}'")
        result = run_flow_from_json(flow="Bajaj HackRx.json", input_value=test_input, tweaks=tweaks, session_id="debug-session")
        
        print("\n--- ✅ SUCCESS! ---")
        print("Flow ran without errors.")
        print("\n--- Full Result ---")
        print(result)

    except Exception as e:
        print("\n--- ❌ AN ERROR OCCURRED ---")
        print("The program crashed. Here is the exact error message:")
        print("-------------------------------------------------")
        # This will print the detailed traceback to help us debug
        import traceback
        traceback.print_exc()
        print("-------------------------------------------------")

print("\n--- Debug Script Finished ---")
