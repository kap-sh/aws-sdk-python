"""Generated from Smithy shape ``com.amazonaws.ssmsap#HostRole``."""

from typing import Literal, TypeAlias, cast

HostRole: TypeAlias = Literal[
    "LEADER",
    "WORKER",
    "STANDBY",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: HostRole) -> str:
    return value


def deserialize_json(data: str) -> HostRole:
    return cast(HostRole, data)
