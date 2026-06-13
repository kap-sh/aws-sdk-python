"""Generated from Smithy shape ``com.amazonaws.backup#RestoreJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

RestoreJobStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "COMPLETED",
    "ABORTED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "RUNNING",
        "COMPLETED",
        "ABORTED",
        "FAILED",
    )
)


def serialize_json(value: RestoreJobStatus) -> str:
    return value


def deserialize_json(data: str) -> RestoreJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RestoreJobStatus value: {data!r}")
    return cast(RestoreJobStatus, data)
