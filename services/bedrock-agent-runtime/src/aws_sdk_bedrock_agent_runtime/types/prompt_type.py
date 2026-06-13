"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PromptType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

PromptType: TypeAlias = Literal[
    "PRE_PROCESSING",
    "ORCHESTRATION",
    "KNOWLEDGE_BASE_RESPONSE_GENERATION",
    "POST_PROCESSING",
    "ROUTING_CLASSIFIER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRE_PROCESSING",
        "ORCHESTRATION",
        "KNOWLEDGE_BASE_RESPONSE_GENERATION",
        "POST_PROCESSING",
        "ROUTING_CLASSIFIER",
    )
)


def serialize_json(value: PromptType) -> str:
    return value


def deserialize_json(data: str) -> PromptType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PromptType value: {data!r}")
    return cast(PromptType, data)
