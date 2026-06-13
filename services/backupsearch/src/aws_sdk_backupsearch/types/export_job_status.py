"""Generated from Smithy shape ``com.amazonaws.backupsearch#ExportJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backupsearch.errors import DeserializationError

ExportJobStatus: TypeAlias = Literal[
    "RUNNING",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: ExportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportJobStatus value: {data!r}")
    return cast(ExportJobStatus, data)
