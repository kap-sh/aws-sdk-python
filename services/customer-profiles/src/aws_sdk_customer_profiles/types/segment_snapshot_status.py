"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentSnapshotStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

SegmentSnapshotStatus: TypeAlias = Literal[
    "COMPLETED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "IN_PROGRESS",
        "FAILED",
    )
)


def serialize_json(value: SegmentSnapshotStatus) -> str:
    return value


def deserialize_json(data: str) -> SegmentSnapshotStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SegmentSnapshotStatus value: {data!r}")
    return cast(SegmentSnapshotStatus, data)
