"""Generated from Smithy shape ``com.amazonaws.ssm#NodeTypeName``."""

from typing import Literal, TypeAlias, cast

NodeTypeName: TypeAlias = Literal["Instance",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeTypeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeTypeName:
    return cast(NodeTypeName, data)
