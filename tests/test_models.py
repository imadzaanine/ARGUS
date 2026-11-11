import pytest
from pydantic import ValidationError

from argus.models import Claim, Paper, RunState


def test_paper_requires_title():
    with pytest.raises(ValidationError):
        Paper(id="1", source="arxiv")


def test_paper_rejects_unknown_source():
    with pytest.raises(ValidationError):
        Paper(id="1", title="X", source="google")


def test_claim_defaults_are_unverified():
    c = Claim(id="c1", sub_q="q1", text="A", quote="B", paper_id="p1")
    assert c.quote_found is None
    assert c.supported is None


def test_runstate_lists_are_not_shared():
    a, b = RunState(question="x"), RunState(question="y")
    a.claims.append(Claim(id="c1", sub_q="q", text="t", quote="u", paper_id="p"))
    assert b.claims == []