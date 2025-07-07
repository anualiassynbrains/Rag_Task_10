FastAPI & Strawberry GraphQL Server

This project implements a powerful **Retrieval-Augmented Generation (RAG)** system designed for querying legal documents. It exposes a modern GraphQL API built with FastAPI and Strawberry, allowing you to ask natural language questions about a corpus of legal case files and receive precise, context-aware answers from an LLM.

  

  

 Technology Stack
-----------------

*   **Backend Framework**: FastAPI
    
*   **GraphQL Library**: Strawberry
    
*   **LLM Orchestration**: LangChain, LangChain-Groq
    
*   **Embedding Model**: Sentence Transformers (all-MiniLM-L6-v2)
    
*   **Vector Math**: NumPy, Scikit-learn
    
*   **LLM Provider**: Groq (for Llama 3)
    
*   **Environment Management**: python-dotenv
    
*     
    
*     
    
*    Getting Started
    ----------------
    
    Follow these steps to set up and run the project locally.
    
    ### 1\. Prerequisites
    
    *   Python 3.8+
        
    *   Git
        
    
    ### 2\. Clone and Setup
    
    First, clone the repository and navigate into the directory:
    
*   Clone the repository  git clone https://github.com/anualiassynbrains/graphqltask\_task\_6
    ```bash
    cd your-repo-name
    ```
3.  Install project dependencies
    ```bash
    poetry add fastapi uvicorn strawberry-graphql
    ```
5.  Activate virtual environment
    ```bash
      poetry shell
*     ```
    

### Configure Environment

The system requires an API key from [Groq](https://www.google.com/url?sa=E&q=https%3A%2F%2Fconsole.groq.com%2Fkeys) to use the LLM.

Create a file named .env in the root of your project and add your key:

### Run the API Server

Now you can start the FastAPI server with Uvicorn:
 ```bash  
poetry run uvicorn src.ragwork.main:app --reload
```
### Example GraphQL Query

Here is an example query you can run to find information about a case and get both the AI-generated answer and the source documents it used.

  

query LegalCaseSearch {

 legalsearch(query: "What was the case about medical malpractice and the doctor's negligence?") {

 answer

 sources {

 document\_id

 section\_type

 original\_text

 }

 }

}

{
  "data": {
    "legalsearch": {
      "answer": "The case involved a patient, Jane Doe, who sued Dr. Alan Smith for medical malpractice. The core of the case was the doctor's failure to diagnose a critical condition in a timely manner, which led to severe health complications for the patient. The verdict was in favor of the plaintiff, awarding damages for medical costs and suffering.",
      "sources": [
        {
          "document_id": "case_12345",
          "section_type": "summary",
          "original_text": "This case concerns a claim of medical malpractice brought by plaintiff Jane Doe against defendant Dr. Alan Smith. The plaintiff alleges that the defendant's negligence in diagnosis resulted in significant harm..."
        },
        {
          "document_id": "case_12345",
          "section_type": "verdict",
          "original_text": "The court finds in favor of the plaintiff, Jane Doe. The defendant, Dr. Alan Smith, is found to be negligent. Damages are awarded in the amount of $500,000 for medical expenses and pain and suffering."
        },
        {
          "document_id": "case_12345",
          "section_type": "facts_of_case",
          "original_text": "On June 10, 2022, Jane Doe presented to Dr. Smith with symptoms of acute abdominal pain. Despite multiple visits, a correct diagnosis of appendicitis was delayed, leading to a ruptured appendix and peritonitis."
        }
      ]
    }
  }
}