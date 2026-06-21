"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentType``."""

from typing import Literal, TypeAlias, cast

EnvironmentType: TypeAlias = Literal[
    "ssh",
    "ec2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentType:
    return cast(EnvironmentType, data)
