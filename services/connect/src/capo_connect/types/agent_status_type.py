"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusType``."""

from typing import Literal, TypeAlias, cast

AgentStatusType: TypeAlias = Literal[
    "ROUTABLE",
    "CUSTOM",
    "OFFLINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusType) -> str:
    return value


def deserialize_json(data: str) -> AgentStatusType:
    return cast(AgentStatusType, data)
