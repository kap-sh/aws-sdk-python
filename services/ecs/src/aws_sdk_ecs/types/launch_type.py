"""Generated from Smithy shape ``com.amazonaws.ecs#LaunchType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

LaunchType: TypeAlias = Literal[
    "EC2",
    "FARGATE",
    "EXTERNAL",
    "MANAGED_INSTANCES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "FARGATE",
        "EXTERNAL",
        "MANAGED_INSTANCES",
    )
)


def serialize_aws_json_1_1(value: LaunchType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LaunchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LaunchType value: {data!r}")
    return cast(LaunchType, data)
