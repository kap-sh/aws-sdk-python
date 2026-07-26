"""Generated from Smithy shape ``com.amazonaws.backup#BackupJobState``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: BackupJobState) -> str:
    return value


def deserialize_json(data: str) -> BackupJobState:
    return cast(BackupJobState, data)
