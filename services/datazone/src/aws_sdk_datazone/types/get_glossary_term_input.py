"""Generated from Smithy shape ``com.amazonaws.datazone#GetGlossaryTermInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_term_id


class GetGlossaryTermInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this business glossary term exists.</p>"""
    identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The ID of the business glossary term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlossaryTermInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGlossaryTermInput:
    out: GetGlossaryTermInput = {}  # type: ignore[typeddict-item]
    return out
