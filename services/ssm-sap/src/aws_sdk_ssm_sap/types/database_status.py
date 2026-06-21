"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseStatus``."""

from typing import Literal, TypeAlias, cast

DatabaseStatus: TypeAlias = Literal[
    "RUNNING",
    "STARTING",
    "STOPPED",
    "WARNING",
    "UNKNOWN",
    "ERROR",
    "STOPPING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseStatus) -> str:
    return value


def deserialize_json(data: str) -> DatabaseStatus:
    return cast(DatabaseStatus, data)
