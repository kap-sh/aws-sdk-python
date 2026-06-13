"""Generated from Smithy shape ``com.amazonaws.backup#ScanJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "COMPLETED",
        "COMPLETED_WITH_ISSUES",
        "RUNNING",
        "FAILED",
        "CANCELED",
        "AGGREGATE_ALL",
        "ANY",
    )
)


def serialize_json(value: ScanJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ScanJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanJobStatus value: {data!r}")
    return cast(ScanJobStatus, data)
