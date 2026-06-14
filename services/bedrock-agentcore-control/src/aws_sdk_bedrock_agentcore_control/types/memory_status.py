"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

MemoryStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "FAILED",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "FAILED",
        "DELETING",
        "UPDATING",
    )
)


def serialize_json(value: MemoryStatus) -> str:
    return value


def deserialize_json(data: str) -> MemoryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemoryStatus value: {data!r}")
    return cast(MemoryStatus, data)
