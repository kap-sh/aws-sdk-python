"""Generated from Smithy shape ``com.amazonaws.networkmonitor#MonitorState``."""

from typing import Literal, TypeAlias, cast

MonitorState: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "INACTIVE",
    "ERROR",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorState) -> str:
    return value


def deserialize_json(data: str) -> MonitorState:
    return cast(MonitorState, data)
