"""Generated from Smithy shape ``com.amazonaws.neptunegraph#SnapshotStatus``."""

from typing import Literal, TypeAlias, cast

SnapshotStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotStatus) -> str:
    return value


def deserialize_json(data: str) -> SnapshotStatus:
    return cast(SnapshotStatus, data)
