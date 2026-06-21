"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentOutputTextFormatType``."""

from typing import Literal, TypeAlias, cast

DocumentOutputTextFormatType: TypeAlias = Literal[
    "PLAIN_TEXT",
    "MARKDOWN",
    "HTML",
    "CSV",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentOutputTextFormatType) -> str:
    return value


def deserialize_json(data: str) -> DocumentOutputTextFormatType:
    return cast(DocumentOutputTextFormatType, data)
