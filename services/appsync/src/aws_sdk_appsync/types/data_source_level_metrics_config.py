"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceLevelMetricsConfig``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

DataSourceLevelMetricsConfig: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DataSourceLevelMetricsConfig) -> str:
    return value


def deserialize_json(data: str) -> DataSourceLevelMetricsConfig:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataSourceLevelMetricsConfig value: {data!r}"
        )
    return cast(DataSourceLevelMetricsConfig, data)
