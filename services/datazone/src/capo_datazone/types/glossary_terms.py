"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryTerms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.glossary_term_id

GlossaryTerms: TypeAlias = list["capo_datazone.types.glossary_term_id.GlossaryTermId"]


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryTerms) -> list:
    return list(value)


def deserialize_json(data: list) -> GlossaryTerms:
    return list(data)
