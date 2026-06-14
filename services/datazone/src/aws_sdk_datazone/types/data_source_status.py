"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DataSourceStatus: TypeAlias = Literal[
    "CREATING",
    "FAILED_CREATION",
    "READY",
    "UPDATING",
    "FAILED_UPDATE",
    "RUNNING",
    "DELETING",
    "FAILED_DELETION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "FAILED_CREATION",
        "READY",
        "UPDATING",
        "FAILED_UPDATE",
        "RUNNING",
        "DELETING",
        "FAILED_DELETION",
    )
)


def serialize_json(value: DataSourceStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceStatus value: {data!r}")
    return cast(DataSourceStatus, data)
