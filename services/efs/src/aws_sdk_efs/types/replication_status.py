"""Generated from Smithy shape ``com.amazonaws.efs#ReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

ReplicationStatus: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "DELETING",
    "ERROR",
    "PAUSED",
    "PAUSING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "ENABLING",
        "DELETING",
        "ERROR",
        "PAUSED",
        "PAUSING",
    )
)


def serialize_json(value: ReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ReplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicationStatus value: {data!r}")
    return cast(ReplicationStatus, data)
