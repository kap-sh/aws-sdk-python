"""Generated from Smithy shape ``com.amazonaws.s3tables#ReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

ReplicationStatus: TypeAlias = Literal[
    "pending",
    "completed",
    "failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "completed",
        "failed",
    )
)


def serialize_json(value: ReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ReplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicationStatus value: {data!r}")
    return cast(ReplicationStatus, data)
