"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

CopyJobStatus: TypeAlias = Literal[
    "CREATED",
    "RUNNING",
    "ABORTING",
    "ABORTED",
    "COMPLETING",
    "COMPLETED",
    "FAILING",
    "FAILED",
    "PARTIAL",
    "AGGREGATE_ALL",
    "ANY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "RUNNING",
        "ABORTING",
        "ABORTED",
        "COMPLETING",
        "COMPLETED",
        "FAILING",
        "FAILED",
        "PARTIAL",
        "AGGREGATE_ALL",
        "ANY",
    )
)


def serialize_json(value: CopyJobStatus) -> str:
    return value


def deserialize_json(data: str) -> CopyJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CopyJobStatus value: {data!r}")
    return cast(CopyJobStatus, data)
