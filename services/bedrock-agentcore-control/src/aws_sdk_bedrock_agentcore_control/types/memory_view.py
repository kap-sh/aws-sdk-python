"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryView``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

MemoryView: TypeAlias = Literal[
    "full",
    "without_decryption",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "full",
        "without_decryption",
    )
)


def serialize_json(value: MemoryView) -> str:
    return value


def deserialize_json(data: str) -> MemoryView:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemoryView value: {data!r}")
    return cast(MemoryView, data)
