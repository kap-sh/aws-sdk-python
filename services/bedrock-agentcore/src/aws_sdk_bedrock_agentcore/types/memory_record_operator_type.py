"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordOperatorType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: MemoryRecordOperatorType) -> str:
    return value


def deserialize_json(data: str) -> MemoryRecordOperatorType:
    return cast(MemoryRecordOperatorType, data)
