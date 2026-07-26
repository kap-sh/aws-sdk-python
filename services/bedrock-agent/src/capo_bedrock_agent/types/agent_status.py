"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentStatus``."""

from typing import Literal, TypeAlias, cast

AgentStatus: TypeAlias = Literal[
    "CREATING",
    "PREPARING",
    "PREPARED",
    "NOT_PREPARED",
    "DELETING",
    "FAILED",
    "VERSIONING",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentStatus:
    return cast(AgentStatus, data)
