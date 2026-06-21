"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeStatus``."""

from typing import Literal, TypeAlias, cast

AgentRuntimeStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "READY",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentRuntimeStatus:
    return cast(AgentRuntimeStatus, data)
