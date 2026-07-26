"""Generated from Smithy shape ``com.amazonaws.efs#ReplicationStatus``."""

from typing import Literal, TypeAlias, cast

ReplicationStatus: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "DELETING",
    "ERROR",
    "PAUSED",
    "PAUSING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ReplicationStatus:
    return cast(ReplicationStatus, data)
