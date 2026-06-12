"""Generated from Smithy shape ``com.amazonaws.appsync#ResolverLevelMetricsConfig``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

ResolverLevelMetricsConfig: TypeAlias = Literal[
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


def serialize_json(value: ResolverLevelMetricsConfig) -> str:
    return value


def deserialize_json(data: str) -> ResolverLevelMetricsConfig:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResolverLevelMetricsConfig value: {data!r}"
        )
    return cast(ResolverLevelMetricsConfig, data)
