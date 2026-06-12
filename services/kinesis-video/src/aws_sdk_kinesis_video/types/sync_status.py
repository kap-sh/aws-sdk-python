"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#SyncStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

SyncStatus: TypeAlias = Literal[
    "SYNCING",
    "ACKNOWLEDGED",
    "IN_SYNC",
    "SYNC_FAILED",
    "DELETING",
    "DELETE_FAILED",
    "DELETING_ACKNOWLEDGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYNCING",
        "ACKNOWLEDGED",
        "IN_SYNC",
        "SYNC_FAILED",
        "DELETING",
        "DELETE_FAILED",
        "DELETING_ACKNOWLEDGED",
    )
)


def serialize_json(value: SyncStatus) -> str:
    return value


def deserialize_json(data: str) -> SyncStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SyncStatus value: {data!r}")
    return cast(SyncStatus, data)
