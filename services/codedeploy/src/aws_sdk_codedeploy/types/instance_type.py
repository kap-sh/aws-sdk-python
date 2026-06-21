"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceType``."""

from typing import Literal, TypeAlias, cast

InstanceType: TypeAlias = Literal[
    "Blue",
    "Green",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceType:
    return cast(InstanceType, data)
