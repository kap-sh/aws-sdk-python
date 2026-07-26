"""Generated from Smithy shape ``com.amazonaws.datazone#GetGlossaryTermInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_term_id


class GetGlossaryTermInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this business glossary term exists.</p>"""
    identifier: "capo_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The ID of the business glossary term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlossaryTermInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGlossaryTermInput:
    out: GetGlossaryTermInput = {}  # type: ignore[typeddict-item]
    return out
