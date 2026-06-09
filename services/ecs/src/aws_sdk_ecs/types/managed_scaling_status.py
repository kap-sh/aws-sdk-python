"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedScalingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

ManagedScalingStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ManagedScalingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedScalingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedScalingStatus value: {data!r}")
    return cast(ManagedScalingStatus, data)
