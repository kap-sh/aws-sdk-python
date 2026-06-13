"""Generated from Smithy shape ``com.amazonaws.datazone#DetailedGlossaryTerms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.detailed_glossary_term

DetailedGlossaryTerms: TypeAlias = list[
    "aws_sdk_datazone.types.detailed_glossary_term.DetailedGlossaryTerm"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetailedGlossaryTerms) -> list:
    import aws_sdk_datazone.types.detailed_glossary_term

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.detailed_glossary_term.serialize_json(item))
    return out


def deserialize_json(data: list) -> DetailedGlossaryTerms:
    import aws_sdk_datazone.types.detailed_glossary_term

    out: DetailedGlossaryTerms = []
    for item in data:
        out.append(aws_sdk_datazone.types.detailed_glossary_term.deserialize_json(item))
    return out
