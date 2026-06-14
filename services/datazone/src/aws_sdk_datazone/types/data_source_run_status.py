"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DataSourceRunStatus: TypeAlias = Literal[
    "REQUESTED",
    "RUNNING",
    "FAILED",
    "PARTIALLY_SUCCEEDED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUESTED",
        "RUNNING",
        "FAILED",
        "PARTIALLY_SUCCEEDED",
        "SUCCESS",
    )
)


def serialize_json(value: DataSourceRunStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceRunStatus value: {data!r}")
    return cast(DataSourceRunStatus, data)
