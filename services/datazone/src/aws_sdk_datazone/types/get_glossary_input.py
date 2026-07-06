"""Generated from Smithy shape ``com.amazonaws.datazone#GetGlossaryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_id


class GetGlossaryInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this business glossary exists.</p>"""
    identifier: "aws_sdk_datazone.types.glossary_id.GlossaryId"
    """<p>The ID of the business glossary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlossaryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGlossaryInput:
    out: GetGlossaryInput = {}  # type: ignore[typeddict-item]
    return out
