"""Generated from Smithy shape ``com.amazonaws.resourcegroups#TagSyncTaskStatus``."""

from typing import Literal, TypeAlias, cast

TagSyncTaskStatus: TypeAlias = Literal[
    "ACTIVE",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: TagSyncTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TagSyncTaskStatus:
    return cast(TagSyncTaskStatus, data)
