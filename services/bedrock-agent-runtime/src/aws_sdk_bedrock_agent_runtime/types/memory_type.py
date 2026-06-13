"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#MemoryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

MemoryType: TypeAlias = Literal["SESSION_SUMMARY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SESSION_SUMMARY",))


def serialize_json(value: MemoryType) -> str:
    return value


def deserialize_json(data: str) -> MemoryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemoryType value: {data!r}")
    return cast(MemoryType, data)
