"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyFilterOperator``."""

from typing import Literal, TypeAlias, cast

InstancePropertyFilterOperator: TypeAlias = Literal[
    "Equal",
    "NotEqual",
    "BeginWith",
    "LessThan",
    "GreaterThan",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePropertyFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstancePropertyFilterOperator:
    return cast(InstancePropertyFilterOperator, data)
