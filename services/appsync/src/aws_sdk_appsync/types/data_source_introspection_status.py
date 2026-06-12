"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

DataSourceIntrospectionStatus: TypeAlias = Literal[
    "PROCESSING",
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROCESSING",
        "FAILED",
        "SUCCESS",
    )
)


def serialize_json(value: DataSourceIntrospectionStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceIntrospectionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataSourceIntrospectionStatus value: {data!r}"
        )
    return cast(DataSourceIntrospectionStatus, data)
