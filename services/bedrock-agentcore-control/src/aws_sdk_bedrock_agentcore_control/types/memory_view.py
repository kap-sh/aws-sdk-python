"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryView``."""

from typing import Literal, TypeAlias, cast

MemoryView: TypeAlias = Literal[
    "full",
    "without_decryption",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryView) -> str:
    return value


def deserialize_json(data: str) -> MemoryView:
    return cast(MemoryView, data)
