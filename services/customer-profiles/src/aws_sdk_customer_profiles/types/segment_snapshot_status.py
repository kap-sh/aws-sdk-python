"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentSnapshotStatus``."""

from typing import Literal, TypeAlias, cast

SegmentSnapshotStatus: TypeAlias = Literal[
    "COMPLETED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentSnapshotStatus) -> str:
    return value


def deserialize_json(data: str) -> SegmentSnapshotStatus:
    return cast(SegmentSnapshotStatus, data)
