"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Route53HealthCheckStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

Route53HealthCheckStatus: TypeAlias = Literal[
    "healthy",
    "unhealthy",
    "unknown",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "healthy",
        "unhealthy",
        "unknown",
    )
)


def serialize_aws_json_1_0(value: Route53HealthCheckStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Route53HealthCheckStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Route53HealthCheckStatus value: {data!r}")
    return cast(Route53HealthCheckStatus, data)
