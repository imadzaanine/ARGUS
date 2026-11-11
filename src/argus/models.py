from typing import Literal

from pydantic import BaseModel, Field


class Paper(BaseModel):
    id: str
    title: str
    source: Literal["openalex", "semantic_scholar", "arxiv"]
    year: int | None = None
    authors: list[str] = Field(default_factory=list)
    doi: str | None = None
    abstract: str | None = None
    url: str | None = None
    pdf_url: str | None = None
    citation_count: int | None = None


class SubQuestion(BaseModel):
    id: str
    text: str
    min_sources: int = 3


class Claim(BaseModel):
    id: str
    sub_q: str
    text: str
    quote: str
    paper_id: str
    quote_found: bool | None = None
    supported: bool | None = None
    confidence: Literal["strong", "moderate", "weak"] | None = None


class RunState(BaseModel):
    question: str
    plan: list[SubQuestion] = Field(default_factory=list)
    candidates: list[Paper] = Field(default_factory=list)
    claims: list[Claim] = Field(default_factory=list)
    retries: dict[str, int] = Field(default_factory=dict)
    trace: list[dict] = Field(default_factory=list)
    report: str | None = None