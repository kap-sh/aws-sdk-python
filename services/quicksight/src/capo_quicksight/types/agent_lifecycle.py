"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentLifecycle``."""

from typing import Literal, TypeAlias, cast

AgentLifecycle: TypeAlias = Literal[
    "PREVIEW",
    "PUBLISHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentLifecycle) -> str:
    return value


def deserialize_json(data: str) -> AgentLifecycle:
    return cast(AgentLifecycle, data)
