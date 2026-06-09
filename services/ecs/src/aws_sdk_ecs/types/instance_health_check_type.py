"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

InstanceHealthCheckType: TypeAlias = Literal[
    "CONTAINER_RUNTIME",
    "ACCELERATED_COMPUTE",
    "DAEMON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTAINER_RUNTIME",
        "ACCELERATED_COMPUTE",
        "DAEMON",
    )
)


def serialize_aws_json_1_1(value: InstanceHealthCheckType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthCheckType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceHealthCheckType value: {data!r}")
    return cast(InstanceHealthCheckType, data)
