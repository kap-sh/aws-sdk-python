"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptType``."""

from typing import Literal, TypeAlias, cast

PromptType: TypeAlias = Literal[
    "PRE_PROCESSING",
    "ORCHESTRATION",
    "POST_PROCESSING",
    "KNOWLEDGE_BASE_RESPONSE_GENERATION",
    "MEMORY_SUMMARIZATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptType) -> str:
    return value


def deserialize_json(data: str) -> PromptType:
    return cast(PromptType, data)
