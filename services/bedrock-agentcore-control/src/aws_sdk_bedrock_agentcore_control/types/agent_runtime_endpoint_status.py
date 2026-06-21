"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeEndpointStatus``."""

from typing import Literal, TypeAlias, cast

AgentRuntimeEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "READY",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentRuntimeEndpointStatus:
    return cast(AgentRuntimeEndpointStatus, data)
