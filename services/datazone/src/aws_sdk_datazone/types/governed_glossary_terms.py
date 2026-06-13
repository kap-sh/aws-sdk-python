"""Generated from Smithy shape ``com.amazonaws.datazone#GovernedGlossaryTerms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glossary_term_id

GovernedGlossaryTerms: TypeAlias = list[
    "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
]


# --- restJson1 ser/de ---
def serialize_json(value: GovernedGlossaryTerms) -> list:
    return list(value)


def deserialize_json(data: list) -> GovernedGlossaryTerms:
    return list(data)
