"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Source``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

Source: TypeAlias = Literal[
    "ACTION_GROUP",
    "KNOWLEDGE_BASE",
    "PARSER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTION_GROUP",
        "KNOWLEDGE_BASE",
        "PARSER",
    )
)


def serialize_json(value: Source) -> str:
    return value


def deserialize_json(data: str) -> Source:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Source value: {data!r}")
    return cast(Source, data)
