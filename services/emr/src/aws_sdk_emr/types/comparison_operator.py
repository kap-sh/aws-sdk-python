"""Generated from Smithy shape ``com.amazonaws.emr#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "GREATER_THAN_OR_EQUAL",
    "GREATER_THAN",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
