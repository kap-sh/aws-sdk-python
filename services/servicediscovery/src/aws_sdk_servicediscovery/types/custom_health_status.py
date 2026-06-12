"""Generated from Smithy shape ``com.amazonaws.servicediscovery#CustomHealthStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

CustomHealthStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_aws_json_1_1(value: CustomHealthStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomHealthStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomHealthStatus value: {data!r}")
    return cast(CustomHealthStatus, data)
