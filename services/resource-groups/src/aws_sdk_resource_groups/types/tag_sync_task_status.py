"""Generated from Smithy shape ``com.amazonaws.resourcegroups#TagSyncTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

TagSyncTaskStatus: TypeAlias = Literal[
    "ACTIVE",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ERROR",
    )
)


def serialize_json(value: TagSyncTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TagSyncTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TagSyncTaskStatus value: {data!r}")
    return cast(TagSyncTaskStatus, data)
