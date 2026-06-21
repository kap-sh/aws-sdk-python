"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseState``."""

from typing import Literal, TypeAlias, cast

KnowledgeBaseState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseState) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseState:
    return cast(KnowledgeBaseState, data)
