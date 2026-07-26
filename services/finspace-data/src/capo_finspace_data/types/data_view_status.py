"""Generated from Smithy shape ``com.amazonaws.finspacedata#DataViewStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DataViewStatus) -> str:
    return value


def deserialize_json(data: str) -> DataViewStatus:
    return cast(DataViewStatus, data)
