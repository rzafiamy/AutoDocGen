import os
import re
from config import Config

class Context:
    def __init__(self, directory, max_chars=Config.MAX_CHARS, max_files=Config.FILE_LIMIT):
        self.directory = directory
        self.max_chars = max_chars
        self.max_files = max_files
        self.files = []
        self.content = ""
    
    def retrieve_files(self):
        """Retrieve and concatenate contents of all files in the directory up to max_chars."""
        files_read = 0
        for root, _, files in os.walk(self.directory):
            for file in files:
                if files_read >= self.max_files:
                    break
                elif file.endswith(tuple(Config.FILE_EXTENSIONS)):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        file_content = f.read()
                        self.files.append(file_path)
                        files_read += 1

                        self.content += "*** " + file_path + " ***\n"
                        # read up to max_chars characters from the file
                        if len(self.content) + len(file_content) <= self.max_chars:
                            self.content += file_content
                        else:
                            remaining_chars = self.max_chars - len(self.content)
                            self.content += file_content[:remaining_chars]
                            break
    
    def get_files(self):
        return self.files

    def normalize_content(self):
        """Normalize the content to reduce token size."""
        self.content = re.sub(r'\s+', ' ', self.content)  # Replace multiple spaces/newlines with a single space
    
    def compute_token_size(self):
        """Compute token size based on the normalized content."""
        words = self.content.split()
        token_size = len(words) / 650 * Config.TOKENS_PER_650_WORDS
        return token_size

# Example usage
if __name__ == "__main__":
    context = Context("example", max_chars=10000, max_files=10)
    context.retrieve_files()

    print(f"Files Read: {context.get_files()}")
    context.normalize_content()
    token_size = context.compute_token_size()
    print(f"Normalized Content: {context.content}")  # Print the first 500 characters for preview
    print(f"Computed Token Size: {token_size} tokens")
