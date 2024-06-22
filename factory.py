from openai import OpenAI
from groq import Groq
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

class LLMInterface:
    def generate_documentation(self, code, detail_level, model, max_tokens):
        raise NotImplementedError("This method should be overridden by subclasses")

#-------------------------------------------
# Implement the LLM classes for OPENAI
#-------------------------------------------
class OpenAILLM(LLMInterface):
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
        )

    def generate_documentation(self, code, detail_level, model="gpt-3.5-turbo-0125", max_tokens=4096):
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a developer. You are writing documentation for a codebase. You need to generate documentation in markdown with headers.",
                },
                {
                    "role": "user",
                    "content": f"Generate {detail_level} documentation for the following code in makdown with headers:\n{code}",
                },
            ],
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

#-------------------------------------------
# Implement the LLM classes for GROQ
#-------------------------------------------
class GroqLLM(LLMInterface):
    def __init__(self, api_key):
        self.client = Groq(
            api_key=api_key,
        )

    def generate_documentation(self, code, detail_level, model="llama3-70b-8192", max_tokens=8192):
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"You are a developer. You are writing documentation for a codebase. You need to generate documentation in markdown with headers.",
                },
                {
                    "role": "user",
                    "content": f"Generate {detail_level} documentation for the following code in makdown with headers:\n{code}",
                },
            ],
            max_tokens=max_tokens,
            model=model,
        )

        return response.choices[0].message.content

#-------------------------------------------
# Implement the LLM classes for MISTRAL
#-------------------------------------------
class MistralLLM(LLMInterface):
    def __init__(self, api_key):
        self.client = MistralClient(
            api_key=api_key,
        )

    def generate_documentation(self, code, detail_level, model="mistral", max_tokens=1500):
        # Implement the call to Mistral API
        
        chat_response = self.client.chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a developer. You are writing documentation for a codebase. You need to generate documentation in markdown with headers.",
                },
                {
                    "role": "user",
                    "content": f"Generate {detail_level} documentation for the following code in makdown with headers:\n{code}",
                },
            ],
        )

        return chat_response.choices[0].message.content


class LLMFactory:
    @staticmethod
    def create_llm(provider, api_key=None, model_path=None):
        if provider == "openai":
            return OpenAILLM(api_key)
        elif provider == "groq":
            return GroqLLM(api_key)
        elif provider == "mistral":
            return MistralLLM(api_key)
        else:
            raise ValueError(f"Unknown provider: {provider}")

# Example usage
if __name__ == "__main__":
    # Example: Create an OpenAI LLM instance and generate documentation
    llm = LLMFactory.create_llm("openai", api_key="your-openai-api-key")
    code_sample = "def add(a, b): return a + b"
    detail_level = "high"
    documentation = llm.generate_documentation(code_sample, detail_level)
    print(documentation)
