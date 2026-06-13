"""Generated from Smithy shape ``com.amazonaws.backup#BackupJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

BackupJobStatus: TypeAlias = Literal[
    "CREATED",
    "PENDING",
    "RUNNING",
    "ABORTING",
    "ABORTED",
    "COMPLETED",
    "FAILED",
    "EXPIRED",
    "PARTIAL",
    "AGGREGATE_ALL",
    "ANY",
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
        "AGGREGATE_ALL",
        "ANY",
    )
)


def serialize_json(value: BackupJobStatus) -> str:
    return value


def deserialize_json(data: str) -> BackupJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupJobStatus value: {data!r}")
    return cast(BackupJobStatus, data)
