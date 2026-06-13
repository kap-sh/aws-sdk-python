"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SnapshotJobStatus: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "RUNNING",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: SnapshotJobStatus) -> str:
    return value


def deserialize_json(data: str) -> SnapshotJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotJobStatus value: {data!r}")
    return cast(SnapshotJobStatus, data)
