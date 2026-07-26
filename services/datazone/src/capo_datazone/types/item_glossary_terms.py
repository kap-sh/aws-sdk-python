"""Generated from Smithy shape ``com.amazonaws.datazone#ItemGlossaryTerms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.glossary_term_id

ItemGlossaryTerms: TypeAlias = list[
    "capo_datazone.types.glossary_term_id.GlossaryTermId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ItemGlossaryTerms) -> list:
    return list(value)


def deserialize_json(data: list) -> ItemGlossaryTerms:
    return list(data)
