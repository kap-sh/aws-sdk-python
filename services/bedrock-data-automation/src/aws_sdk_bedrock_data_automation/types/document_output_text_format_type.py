"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentOutputTextFormatType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

DocumentOutputTextFormatType: TypeAlias = Literal[
    "PLAIN_TEXT",
    "MARKDOWN",
    "HTML",
    "CSV",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PLAIN_TEXT",
        "MARKDOWN",
        "HTML",
        "CSV",
    )
)


def serialize_json(value: DocumentOutputTextFormatType) -> str:
    return value


def deserialize_json(data: str) -> DocumentOutputTextFormatType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DocumentOutputTextFormatType value: {data!r}"
        )
    return cast(DocumentOutputTextFormatType, data)
