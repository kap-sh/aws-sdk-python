"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#HealthCheckProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_global_accelerator.errors import DeserializationError

HealthCheckProtocol: TypeAlias = Literal[
    "TCP",
    "HTTP",
    "HTTPS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TCP",
        "HTTP",
        "HTTPS",
    )
)


def serialize_aws_json_1_1(value: HealthCheckProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthCheckProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HealthCheckProtocol value: {data!r}")
    return cast(HealthCheckProtocol, data)
