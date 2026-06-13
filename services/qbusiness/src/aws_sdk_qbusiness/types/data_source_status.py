"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

DataSourceStatus: TypeAlias = Literal[
    "PENDING_CREATION",
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_CREATION",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
        "UPDATING",
    )
)


def serialize_json(value: DataSourceStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceStatus value: {data!r}")
    return cast(DataSourceStatus, data)
