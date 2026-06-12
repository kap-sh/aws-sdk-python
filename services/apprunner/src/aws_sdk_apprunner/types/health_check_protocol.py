"""Generated from Smithy shape ``com.amazonaws.apprunner#HealthCheckProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

HealthCheckProtocol: TypeAlias = Literal[
    "TCP",
    "HTTP",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TCP",
        "HTTP",
    )
)


def serialize_aws_json_1_0(value: HealthCheckProtocol) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HealthCheckProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HealthCheckProtocol value: {data!r}")
    return cast(HealthCheckProtocol, data)
