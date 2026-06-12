"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HealthCheckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

HealthCheckType: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
    "TCP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP",
        "HTTPS",
        "TCP",
    )
)


def serialize_aws_json_1_1(value: HealthCheckType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthCheckType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HealthCheckType value: {data!r}")
    return cast(HealthCheckType, data)
