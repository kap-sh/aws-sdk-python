"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceLevelMetricsBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

DataSourceLevelMetricsBehavior: TypeAlias = Literal[
    "FULL_REQUEST_DATA_SOURCE_METRICS",
    "PER_DATA_SOURCE_METRICS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_REQUEST_DATA_SOURCE_METRICS",
        "PER_DATA_SOURCE_METRICS",
    )
)


def serialize_json(value: DataSourceLevelMetricsBehavior) -> str:
    return value


def deserialize_json(data: str) -> DataSourceLevelMetricsBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataSourceLevelMetricsBehavior value: {data!r}"
        )
    return cast(DataSourceLevelMetricsBehavior, data)
