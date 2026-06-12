"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ChunkingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ChunkingStrategy: TypeAlias = Literal[
    "FIXED_SIZE",
    "NONE",
    "HIERARCHICAL",
    "SEMANTIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIXED_SIZE",
        "NONE",
        "HIERARCHICAL",
        "SEMANTIC",
    )
)


def serialize_json(value: ChunkingStrategy) -> str:
    return value


def deserialize_json(data: str) -> ChunkingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChunkingStrategy value: {data!r}")
    return cast(ChunkingStrategy, data)
