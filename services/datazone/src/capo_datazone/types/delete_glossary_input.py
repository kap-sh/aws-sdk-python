"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteGlossaryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_id


class DeleteGlossaryInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the business glossary is deleted.</p>"""
    identifier: "capo_datazone.types.glossary_id.GlossaryId"
    """<p>The ID of the business glossary that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGlossaryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGlossaryInput:
    out: DeleteGlossaryInput = {}  # type: ignore[typeddict-item]
    return out
