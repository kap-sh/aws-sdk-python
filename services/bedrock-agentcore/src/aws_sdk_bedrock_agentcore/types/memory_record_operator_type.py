"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

MemoryRecordOperatorType: TypeAlias = Literal[
    "EQUALS_TO",
    "EXISTS",
    "NOT_EXISTS",
    "BEFORE",
    "AFTER",
    "CONTAINS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS_TO",
        "EXISTS",
        "NOT_EXISTS",
        "BEFORE",
        "AFTER",
        "CONTAINS",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUALS",
        "LESS_THAN",
        "LESS_THAN_OR_EQUALS",
    )
)


def serialize_json(value: MemoryRecordOperatorType) -> str:
    return value


def deserialize_json(data: str) -> MemoryRecordOperatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemoryRecordOperatorType value: {data!r}")
    return cast(MemoryRecordOperatorType, data)
