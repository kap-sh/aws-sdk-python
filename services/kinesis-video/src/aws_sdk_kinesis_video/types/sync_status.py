"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#SyncStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SyncStatus) -> str:
    return value


def deserialize_json(data: str) -> SyncStatus:
    return cast(SyncStatus, data)
