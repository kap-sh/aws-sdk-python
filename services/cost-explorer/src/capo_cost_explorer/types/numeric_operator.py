"""Generated from Smithy shape ``com.amazonaws.costexplorer#NumericOperator``."""

from typing import Literal, TypeAlias, cast

NumericOperator: TypeAlias = Literal[
    "EQUAL",
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN_OR_EQUAL",
    "GREATER_THAN",
    "LESS_THAN",
    "BETWEEN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NumericOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NumericOperator:
    return cast(NumericOperator, data)
