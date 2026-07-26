"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ChunkingStrategy``."""

from typing import Literal, TypeAlias, cast

ChunkingStrategy: TypeAlias = Literal[
    "FIXED_SIZE",
    "NONE",
    "HIERARCHICAL",
    "SEMANTIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChunkingStrategy) -> str:
    return value


def deserialize_json(data: str) -> ChunkingStrategy:
    return cast(ChunkingStrategy, data)
