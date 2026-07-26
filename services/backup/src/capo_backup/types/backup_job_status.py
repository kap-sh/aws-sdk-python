"""Generated from Smithy shape ``com.amazonaws.backup#BackupJobStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: BackupJobStatus) -> str:
    return value


def deserialize_json(data: str) -> BackupJobStatus:
    return cast(BackupJobStatus, data)
