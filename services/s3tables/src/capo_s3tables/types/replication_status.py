"""Generated from Smithy shape ``com.amazonaws.s3tables#ReplicationStatus``."""

from typing import Literal, TypeAlias, cast

ReplicationStatus: TypeAlias = Literal[
    "pending",
    "completed",
    "failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ReplicationStatus:
    return cast(ReplicationStatus, data)
