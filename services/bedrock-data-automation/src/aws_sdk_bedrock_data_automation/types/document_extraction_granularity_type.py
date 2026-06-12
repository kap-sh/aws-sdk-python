"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentExtractionGranularityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

DocumentExtractionGranularityType: TypeAlias = Literal[
    "DOCUMENT",
    "PAGE",
    "ELEMENT",
    "WORD",
    "LINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOCUMENT",
        "PAGE",
        "ELEMENT",
        "WORD",
        "LINE",
    )
)


def serialize_json(value: DocumentExtractionGranularityType) -> str:
    return value


def deserialize_json(data: str) -> DocumentExtractionGranularityType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DocumentExtractionGranularityType value: {data!r}"
        )
    return cast(DocumentExtractionGranularityType, data)
