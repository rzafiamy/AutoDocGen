class Config:
    # File settings
    FILE_EXTENSIONS = [".c", ".h"]  # List of file extensions to consider
    FILE_LIMIT = 5  # Maximum number of files to read
    MAX_CHARS = 10000  # Maximum number of characters to read per file

    # Token size computation
    TOKENS_PER_650_WORDS = 1000

    # LLM settings
    DEFAULT_PROVIDER = "openai"
    DEFAULT_API_KEY = "your-default-api-key"

    # OUTPUT settings
    OUTPUT_DIR = "out"
