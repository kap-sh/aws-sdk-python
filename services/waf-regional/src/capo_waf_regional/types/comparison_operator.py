"""Generated from Smithy shape ``com.amazonaws.wafregional#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "EQ",
    "NE",
    "LE",
    "LT",
    "GE",
    "GT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
