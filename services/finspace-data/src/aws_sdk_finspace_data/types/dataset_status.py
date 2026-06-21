"""Generated from Smithy shape ``com.amazonaws.finspacedata#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

"""Status of the dataset process returned from scheduler service."""
DatasetStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "SUCCESS",
    "RUNNING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetStatus) -> str:
    return value


def deserialize_json(data: str) -> DatasetStatus:
    return cast(DatasetStatus, data)
