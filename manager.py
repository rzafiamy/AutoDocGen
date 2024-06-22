import argparse
import os
from factory import LLMFactory
from context import Context
from generator import Generator

def main():
    parser = argparse.ArgumentParser(description="Generate code documentation using various LLMs")
    parser.add_argument('--code', type=str, help='Path to the folder containing code files')
    parser.add_argument('--provider', type=str, choices=['openai', 'groq', 'mistral'], required=True, help='LLM provider')
    parser.add_argument('--token', type=str, help='API key for the LLM provider')
    parser.add_argument('--num_files', type=int, help='Number of files to read', default=10)
    parser.add_argument('--max_chars', type=int, help='Maximum number of characters to read from each file', default=10000)

    args = parser.parse_args()

    # Create a context object
    context = Context(args.code, max_chars=args.max_chars, max_files=args.num_files)
    context.retrieve_files()
    context.normalize_content()
    token_size = context.compute_token_size()

    print(f"Files Read: {context.get_files()}")
    print(f"Normalized Content: {context.content[:500]}")  # Print the first 500 characters for preview
    print(f"Computed Token Size: {token_size} tokens")

    # Create an LLM instance based on the provider
    llm = LLMFactory.create_llm(args.provider, api_key=args.token)
    documentation = llm.generate_documentation(context.content, detail_level="detailed")
    
    # Generate a DOCX file with the documentation
    generator = Generator(documentation)
    print(generator.generate_docx("output.docx"))




if __name__ == "__main__":
    main()
