"""Generated from Smithy shape ``com.amazonaws.eventbridge#LaunchType``."""

from typing import Literal, TypeAlias, cast

LaunchType: TypeAlias = Literal[
    "EC2",
    "FARGATE",
    "EXTERNAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LaunchType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LaunchType:
    return cast(LaunchType, data)
