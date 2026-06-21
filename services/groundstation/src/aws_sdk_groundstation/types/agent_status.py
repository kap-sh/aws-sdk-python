"""Generated from Smithy shape ``com.amazonaws.groundstation#AgentStatus``."""

from typing import Literal, TypeAlias, cast

AgentStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentStatus:
    return cast(AgentStatus, data)
