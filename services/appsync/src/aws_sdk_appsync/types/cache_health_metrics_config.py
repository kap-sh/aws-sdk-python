"""Generated from Smithy shape ``com.amazonaws.appsync#CacheHealthMetricsConfig``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

CacheHealthMetricsConfig: TypeAlias = Literal[
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


def serialize_json(value: CacheHealthMetricsConfig) -> str:
    return value


def deserialize_json(data: str) -> CacheHealthMetricsConfig:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CacheHealthMetricsConfig value: {data!r}")
    return cast(CacheHealthMetricsConfig, data)
