"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#HealthStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_dashboards.errors import DeserializationError

HealthStatusCode: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_aws_json_1_0(value: HealthStatusCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HealthStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HealthStatusCode value: {data!r}")
    return cast(HealthStatusCode, data)
