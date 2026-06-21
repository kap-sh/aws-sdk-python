"""Generated from Smithy shape ``com.amazonaws.connect#AgentAvailabilityTimer``."""

from typing import Literal, TypeAlias, cast

AgentAvailabilityTimer: TypeAlias = Literal[
    "TIME_SINCE_LAST_ACTIVITY",
    "TIME_SINCE_LAST_INBOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentAvailabilityTimer) -> str:
    return value


def deserialize_json(data: str) -> AgentAvailabilityTimer:
    return cast(AgentAvailabilityTimer, data)
