"""Generated from Smithy shape ``com.amazonaws.ssmsap#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

ClusterStatus: TypeAlias = Literal[
    "ONLINE",
    "STANDBY",
    "MAINTENANCE",
    "OFFLINE",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> ClusterStatus:
    return cast(ClusterStatus, data)
