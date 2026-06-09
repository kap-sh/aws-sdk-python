"""Generated from Smithy shape ``com.amazonaws.ecs#HealthStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

HealthStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: HealthStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HealthStatus value: {data!r}")
    return cast(HealthStatus, data)
