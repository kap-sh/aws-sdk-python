"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationType``."""

from typing import Literal, TypeAlias, cast

InvocationType: TypeAlias = Literal[
    "ACTION_GROUP",
    "KNOWLEDGE_BASE",
    "FINISH",
    "ACTION_GROUP_CODE_INTERPRETER",
    "AGENT_COLLABORATOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvocationType) -> str:
    return value


def deserialize_json(data: str) -> InvocationType:
    return cast(InvocationType, data)
