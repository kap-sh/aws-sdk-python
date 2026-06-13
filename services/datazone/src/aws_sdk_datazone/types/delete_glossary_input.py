"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteGlossaryInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_id


class DeleteGlossaryInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the business glossary is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.glossary_id.GlossaryId"
    """<p>The ID of the business glossary that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGlossaryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGlossaryInput:
    out: DeleteGlossaryInput = {}  # type: ignore[typeddict-item]
    return out
