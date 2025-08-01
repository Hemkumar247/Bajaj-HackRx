import os
from dotenv import load_dotenv

# Load environment variables from .env file
# The load_dotenv() function will search for a .env file in the current directory
# and load the variables from it into the environment.
load_dotenv()

print("--- Environment Variable Check ---")

# Check for GOOGLE_API_KEY
google_key = os.getenv("GOOGLE_API_KEY")
if google_key:
    # To protect your key, we'll only show the first few and last few characters
    print(f"✅ GOOGLE_API_KEY found: {google_key[:4]}...{google_key[-4:]}")
else:
    print("❌ GOOGLE_API_KEY not found.")

# Check for OPENAI_API_KEY
openai_key = os.getenv("OPENAI_API_KEY")
if openai_key:
    print(f"✅ OPENAI_API_KEY found: {openai_key[:4]}...{openai_key[-4:]}")
else:
    print("❌ OPENAI_API_KEY not found.")

print("\n--- Check Finished ---")
print("If keys are not found, please double-check your .env file for any formatting errors (e.g., extra spaces, quotes).")
