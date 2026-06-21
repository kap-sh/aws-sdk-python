"""Generated from Smithy shape ``com.amazonaws.backup#ScanJobStatus``."""

from typing import Literal, TypeAlias, cast

ScanJobStatus: TypeAlias = Literal[
    "CREATED",
    "COMPLETED",
    "COMPLETED_WITH_ISSUES",
    "RUNNING",
    "FAILED",
    "CANCELED",
    "AGGREGATE_ALL",
    "ANY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ScanJobStatus:
    return cast(ScanJobStatus, data)
