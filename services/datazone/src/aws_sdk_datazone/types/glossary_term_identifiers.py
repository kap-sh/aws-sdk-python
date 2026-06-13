"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryTermIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glossary_term_id

GlossaryTermIdentifiers: TypeAlias = list[
    "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
]


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryTermIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> GlossaryTermIdentifiers:
    return list(data)
