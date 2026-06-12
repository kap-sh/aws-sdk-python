"""Generated from Smithy shape ``com.amazonaws.finspacedata#DataViewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

"""Status of a DataView"""
DataViewStatus: TypeAlias = Literal[
    "RUNNING",
    "STARTING",
    "FAILED",
    "CANCELLED",
    "TIMEOUT",
    "SUCCESS",
    "PENDING",
    "FAILED_CLEANUP_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "STARTING",
        "FAILED",
        "CANCELLED",
        "TIMEOUT",
        "SUCCESS",
        "PENDING",
        "FAILED_CLEANUP_FAILED",
    )
)


def serialize_json(value: DataViewStatus) -> str:
    return value


def deserialize_json(data: str) -> DataViewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataViewStatus value: {data!r}")
    return cast(DataViewStatus, data)
