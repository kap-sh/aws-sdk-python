"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#LaunchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_events.errors import DeserializationError

LaunchType: TypeAlias = Literal[
    "EC2",
    "FARGATE",
    "EXTERNAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "FARGATE",
        "EXTERNAL",
    )
)


def serialize_aws_json_1_1(value: LaunchType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LaunchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LaunchType value: {data!r}")
    return cast(LaunchType, data)
