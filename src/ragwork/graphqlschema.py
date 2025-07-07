

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List, Optional
from retriever import run_query

@strawberry.type
class SourceChunk:
    document_id: str
    section_type: str
    original_text: str

@strawberry.type
class LegalSearchResult:
    answer: Optional[str]
    sources: Optional[List[SourceChunk]]

@strawberry.type
class Query:
    @strawberry.field
    def legalsearch(self, query: str, return_answer: bool = True, return_sources: bool = True) -> LegalSearchResult:
        answer, chunks = run_query(query)

        sources = [
            SourceChunk(
                document_id=chunk["document_id"],
                section_type=chunk["section_type"],
                original_text=chunk["text"]
            ) for chunk in chunks
        ] if return_sources else None

        return LegalSearchResult(
            answer=answer if return_answer else None,
            sources=sources
        )

