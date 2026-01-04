import typer                                                    # CLI framework to turn functions into command-line commands
from typing import Optional, List                               # Type hints for clarity and readability
from phi.agent import Agent                                     # Core Phi agent that handles conversations
from phi.storage.agent.postgres import PgAgentStorage           # Stores chat history in Postgres
from phi.knowledge.pdf import PDFUrlKnowledgeBase               # Loads PDFs from URLs into a knowledge base
from phi.vectordb.pgvector import PgVector2                     # Vector database using pgvector
from phi.model.openai import OpenAIChat                         # OpenAI LLM wrapper
from phi.embedder.openai import OpenAIEmbedder                  # OpenAI embedding model
import warnings                                                 # Used to control warning messages
warnings.filterwarnings("ignore", category=FutureWarning)       # Hide future/deprecation warnings


import os                                   # Used for environment variables
from dotenv import load_dotenv              # Loads variables from .env file
load_dotenv()                               # Makes .env variables available to the program

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Read OpenAI API key from environment
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set")  # Stop execution if key is missing

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"  # Postgres connection string

embedder = OpenAIEmbedder(model="text-embedding-3-small")               # Creates embedding model (1536 dims)
storage = PgAgentStorage(table_name="pdf_assistants", db_url=db_url)    # Chat history storage

storage = PgAgentStorage(table_name="pdf_assistants", db_url=db_url)    # Re-initializes same storage


def collect_pdf_urls() -> List[str]:                                    # Function to collect multiple PDF URLs from the user
    urls: List[str] = []                                                # List to store user-provided PDF URLs
    print("\nEnter PDF URLs to load.\n")                                # Instruction message

    while True:                                                         # Loop until user chooses to stop
        url = input("PDF URL: ").strip()                                # Ask user for a PDF URL
        if not url:
            print("Please enter a valid URL.")                          # Validate non-empty input
            continue

        urls.append(url)                                                # Add valid URL to list

        more = input("Add another PDF? (y/n): ").strip().lower()        # Ask if more PDFs are needed
        if more not in ("y", "yes"):
            break                                                       # Exit loop if user says no

    return urls                                                         # Return all collected PDF URLs


def pdf_assistant(new: bool = False, user: str = "user"):               # Main CLI command function
    run_id: Optional[str] = None                                        # Session/run identifier (None = new run)

    urls = collect_pdf_urls()                                           # Collect PDF URLs before starting the assistant

    knowledge_base = PDFUrlKnowledgeBase(                               # Create knowledge base from user PDFs
        urls=urls,
        vector_db=PgVector2(
            collection="pdfs",                                          # Name of pgvector collection/table
            db_url=db_url,
            embedder=embedder
        )
    )

    knowledge_base.load(recreate=True)  # Download PDFs, embed content, store vectors

    assistant = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),     # LLM used to answer questions
        run_id=run_id,                          # Run/session ID
        user_id=user,                           # User identifier for chat history
        knowledge_base=knowledge_base,          # Knowledge base used for retrieval
        storage=storage,                        # Persistent chat storage
        show_tool_calls=True,                   # Show internal tool usage
        search_knowledge=True,                  # Enable searching the knowledge base
        read_chat_history=True,                 # Allow reading previous messages
    )

    if run_id is None:
        run_id = assistant.run_id               # Get generated run ID
        print(f"Started Run: {run_id}")         # Print run ID
    else:
        print(f"Continuing Run: {run_id}")      # Resume existing run

    assistant.cli_app(markdown=True)            # Start interactive CLI chat


if __name__ == "__main__":
    typer.run(pdf_assistant)                    # Run the CLI app
