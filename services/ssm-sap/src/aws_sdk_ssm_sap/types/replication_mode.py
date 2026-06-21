"""Generated from Smithy shape ``com.amazonaws.ssmsap#ReplicationMode``."""

from typing import Literal, TypeAlias, cast

ReplicationMode: TypeAlias = Literal[
    "PRIMARY",
    "NONE",
    "SYNC",
    "SYNCMEM",
    "ASYNC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationMode) -> str:
    return value


def deserialize_json(data: str) -> ReplicationMode:
    return cast(ReplicationMode, data)
