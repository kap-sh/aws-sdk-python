"""Generated from Smithy shape ``com.amazonaws.dynamodb#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "EQ",
    "NE",
    "IN",
    "LE",
    "LT",
    "GE",
    "GT",
    "BETWEEN",
    "NOT_NULL",
    "NULL",
    "CONTAINS",
    "NOT_CONTAINS",
    "BEGINS_WITH",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
