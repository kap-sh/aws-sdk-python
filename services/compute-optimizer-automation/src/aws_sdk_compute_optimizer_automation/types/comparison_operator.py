"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "StringEquals",
    "StringNotEquals",
    "StringEqualsIgnoreCase",
    "StringNotEqualsIgnoreCase",
    "StringLike",
    "StringNotLike",
    "NumericEquals",
    "NumericNotEquals",
    "NumericLessThan",
    "NumericLessThanEquals",
    "NumericGreaterThan",
    "NumericGreaterThanEquals",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
