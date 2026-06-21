"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PromptType``."""

from typing import Literal, TypeAlias, cast

PromptType: TypeAlias = Literal[
    "PRE_PROCESSING",
    "ORCHESTRATION",
    "KNOWLEDGE_BASE_RESPONSE_GENERATION",
    "POST_PROCESSING",
    "ROUTING_CLASSIFIER",
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptType) -> str:
    return value


def deserialize_json(data: str) -> PromptType:
    return cast(PromptType, data)
