"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Type``."""

from typing import Literal, TypeAlias, cast

Type: TypeAlias = Literal[
    "ACTION_GROUP",
    "AGENT_COLLABORATOR",
    "KNOWLEDGE_BASE",
    "FINISH",
    "ASK_USER",
    "REPROMPT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    return cast(Type, data)
