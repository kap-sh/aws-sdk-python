"""Generated from Smithy shape ``com.amazonaws.ssm#NodeFilterOperatorType``."""

from typing import Literal, TypeAlias, cast

NodeFilterOperatorType: TypeAlias = Literal[
    "Equal",
    "NotEqual",
    "BeginWith",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeFilterOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeFilterOperatorType:
    return cast(NodeFilterOperatorType, data)
