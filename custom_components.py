from langflow.custom import Component
from langchain_openai import OpenAIEmbeddings
from langflow.field_typing import Embeddings

class CustomOpenAIEmbeddings(Component):
    display_name = "Custom OpenAI Embeddings"
    description = "A custom component that wraps OpenAIEmbeddings and sets the user_id."

    def build_config(self):
        return {
            "openai_api_key": {"display_name": "OpenAI API Key", "required": True, "password": True},
            "model": {"display_name": "Model", "options": ["text-embedding-3-small", "text-embedding-3-large", "text-embedding-ada-002"], "value": "text-embedding-3-small"},
            "user_id": {"display_name": "User ID", "required": True}
        }

    def build(self, openai_api_key: str, model: str, user_id: str) -> Embeddings:
        return OpenAIEmbeddings(
            openai_api_key=openai_api_key,
            model=model,
            model_kwargs={"user": user_id}
        )
