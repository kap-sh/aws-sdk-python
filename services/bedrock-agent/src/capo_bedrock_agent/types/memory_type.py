"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MemoryType``."""

from typing import Literal, TypeAlias, cast

MemoryType: TypeAlias = Literal["SESSION_SUMMARY",]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryType) -> str:
    return value


def deserialize_json(data: str) -> MemoryType:
    return cast(MemoryType, data)
