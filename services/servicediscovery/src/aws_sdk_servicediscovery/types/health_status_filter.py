"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HealthStatusFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

HealthStatusFilter: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "ALL",
    "HEALTHY_OR_ELSE_ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
        "ALL",
        "HEALTHY_OR_ELSE_ALL",
    )
)


def serialize_aws_json_1_1(value: HealthStatusFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthStatusFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HealthStatusFilter value: {data!r}")
    return cast(HealthStatusFilter, data)
