"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobStatus``."""

from typing import Literal, TypeAlias, cast

SnapshotJobStatus: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobStatus) -> str:
    return value


def deserialize_json(data: str) -> SnapshotJobStatus:
    return cast(SnapshotJobStatus, data)
