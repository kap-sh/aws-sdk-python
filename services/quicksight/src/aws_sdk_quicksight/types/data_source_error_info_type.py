"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceErrorInfoType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSourceErrorInfoType: TypeAlias = Literal[
    "ACCESS_DENIED",
    "COPY_SOURCE_NOT_FOUND",
    "TIMEOUT",
    "ENGINE_VERSION_NOT_SUPPORTED",
    "UNKNOWN_HOST",
    "GENERIC_SQL_FAILURE",
    "CONFLICT",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESS_DENIED",
        "COPY_SOURCE_NOT_FOUND",
        "TIMEOUT",
        "ENGINE_VERSION_NOT_SUPPORTED",
        "UNKNOWN_HOST",
        "GENERIC_SQL_FAILURE",
        "CONFLICT",
        "UNKNOWN",
    )
)


def serialize_json(value: DataSourceErrorInfoType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceErrorInfoType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceErrorInfoType value: {data!r}")
    return cast(DataSourceErrorInfoType, data)
