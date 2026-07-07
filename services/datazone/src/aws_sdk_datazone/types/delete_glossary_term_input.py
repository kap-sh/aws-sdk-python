"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteGlossaryTermInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_term_id


class DeleteGlossaryTermInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the business glossary term is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The ID of the business glossary term that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGlossaryTermInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGlossaryTermInput:
    out: DeleteGlossaryTermInput = {}  # type: ignore[typeddict-item]
    return out
