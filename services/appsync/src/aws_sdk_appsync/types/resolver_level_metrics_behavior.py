"""Generated from Smithy shape ``com.amazonaws.appsync#ResolverLevelMetricsBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

ResolverLevelMetricsBehavior: TypeAlias = Literal[
    "FULL_REQUEST_RESOLVER_METRICS",
    "PER_RESOLVER_METRICS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_REQUEST_RESOLVER_METRICS",
        "PER_RESOLVER_METRICS",
    )
)


def serialize_json(value: ResolverLevelMetricsBehavior) -> str:
    return value


def deserialize_json(data: str) -> ResolverLevelMetricsBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResolverLevelMetricsBehavior value: {data!r}"
        )
    return cast(ResolverLevelMetricsBehavior, data)
