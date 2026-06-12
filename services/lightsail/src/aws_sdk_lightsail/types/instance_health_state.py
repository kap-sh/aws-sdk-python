"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

InstanceHealthState: TypeAlias = Literal[
    "initial",
    "healthy",
    "unhealthy",
    "unused",
    "draining",
    "unavailable",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "initial",
        "healthy",
        "unhealthy",
        "unused",
        "draining",
        "unavailable",
    )
)


def serialize_aws_json_1_1(value: InstanceHealthState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceHealthState value: {data!r}")
    return cast(InstanceHealthState, data)
