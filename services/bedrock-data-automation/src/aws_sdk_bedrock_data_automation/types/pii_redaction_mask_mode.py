"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#PIIRedactionMaskMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Mode for redacting detected PII"""
PIIRedactionMaskMode: TypeAlias = Literal[
    "PII",
    "ENTITY_TYPE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PII",
        "ENTITY_TYPE",
    )
)


def serialize_json(value: PIIRedactionMaskMode) -> str:
    return value


def deserialize_json(data: str) -> PIIRedactionMaskMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PIIRedactionMaskMode value: {data!r}")
    return cast(PIIRedactionMaskMode, data)
