"""Generated from Smithy shape ``com.amazonaws.appsync#OperationLevelMetricsConfig``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

OperationLevelMetricsConfig: TypeAlias = Literal[
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


def serialize_json(value: OperationLevelMetricsConfig) -> str:
    return value


def deserialize_json(data: str) -> OperationLevelMetricsConfig:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OperationLevelMetricsConfig value: {data!r}"
        )
    return cast(OperationLevelMetricsConfig, data)
