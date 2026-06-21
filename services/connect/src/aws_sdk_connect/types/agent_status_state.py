"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusState``."""

from typing import Literal, TypeAlias, cast

AgentStatusState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusState) -> str:
    return value


def deserialize_json(data: str) -> AgentStatusState:
    return cast(AgentStatusState, data)
