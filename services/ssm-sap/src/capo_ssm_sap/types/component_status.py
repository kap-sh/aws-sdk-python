"""Generated from Smithy shape ``com.amazonaws.ssmsap#ComponentStatus``."""

from typing import Literal, TypeAlias, cast

ComponentStatus: TypeAlias = Literal[
    "ACTIVATED",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "RUNNING",
    "RUNNING_WITH_ERROR",
    "UNDEFINED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentStatus) -> str:
    return value


def deserialize_json(data: str) -> ComponentStatus:
    return cast(ComponentStatus, data)
