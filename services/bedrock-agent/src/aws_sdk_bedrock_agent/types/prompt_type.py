"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

PromptType: TypeAlias = Literal[
    "PRE_PROCESSING",
    "ORCHESTRATION",
    "POST_PROCESSING",
    "KNOWLEDGE_BASE_RESPONSE_GENERATION",
    "MEMORY_SUMMARIZATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRE_PROCESSING",
        "ORCHESTRATION",
        "POST_PROCESSING",
        "KNOWLEDGE_BASE_RESPONSE_GENERATION",
        "MEMORY_SUMMARIZATION",
    )
)


def serialize_json(value: PromptType) -> str:
    return value


def deserialize_json(data: str) -> PromptType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PromptType value: {data!r}")
    return cast(PromptType, data)
