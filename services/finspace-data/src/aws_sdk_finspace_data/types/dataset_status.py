"""Generated from Smithy shape ``com.amazonaws.finspacedata#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

"""Status of the dataset process returned from scheduler service."""
DatasetStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "SUCCESS",
    "RUNNING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "FAILED",
        "SUCCESS",
        "RUNNING",
    )
)


def serialize_json(value: DatasetStatus) -> str:
    return value


def deserialize_json(data: str) -> DatasetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetStatus value: {data!r}")
    return cast(DatasetStatus, data)
