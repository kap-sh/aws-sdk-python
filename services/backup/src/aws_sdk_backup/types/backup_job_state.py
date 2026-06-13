"""Generated from Smithy shape ``com.amazonaws.backup#BackupJobState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

BackupJobState: TypeAlias = Literal[
    "CREATED",
    "PENDING",
    "RUNNING",
    "ABORTING",
    "ABORTED",
    "COMPLETED",
    "FAILED",
    "EXPIRED",
    "PARTIAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "PENDING",
        "RUNNING",
        "ABORTING",
        "ABORTED",
        "COMPLETED",
        "FAILED",
        "EXPIRED",
        "PARTIAL",
    )
)


def serialize_json(value: BackupJobState) -> str:
    return value


def deserialize_json(data: str) -> BackupJobState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupJobState value: {data!r}")
    return cast(BackupJobState, data)
