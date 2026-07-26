"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetFilterName``."""

from typing import Literal, TypeAlias, cast

TargetFilterName: TypeAlias = Literal[
    "TargetStatus",
    "ServerInstanceLabel",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetFilterName:
    return cast(TargetFilterName, data)
