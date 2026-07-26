"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentExtractionGranularityType``."""

from typing import Literal, TypeAlias, cast

DocumentExtractionGranularityType: TypeAlias = Literal[
    "DOCUMENT",
    "PAGE",
    "ELEMENT",
    "WORD",
    "LINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentExtractionGranularityType) -> str:
    return value


def deserialize_json(data: str) -> DocumentExtractionGranularityType:
    return cast(DocumentExtractionGranularityType, data)
