"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

MemoryRecordStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_json(value: MemoryRecordStatus) -> str:
    return value


def deserialize_json(data: str) -> MemoryRecordStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemoryRecordStatus value: {data!r}")
    return cast(MemoryRecordStatus, data)
