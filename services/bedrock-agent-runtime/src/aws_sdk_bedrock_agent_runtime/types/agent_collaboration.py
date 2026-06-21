"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboration``."""

from typing import Literal, TypeAlias, cast

AgentCollaboration: TypeAlias = Literal[
    "SUPERVISOR",
    "SUPERVISOR_ROUTER",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboration) -> str:
    return value


def deserialize_json(data: str) -> AgentCollaboration:
    return cast(AgentCollaboration, data)
