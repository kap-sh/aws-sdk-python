"""Generated from Smithy shape ``com.amazonaws.glue#FilterLogicalOperator``."""

from typing import Literal, TypeAlias, cast

FilterLogicalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterLogicalOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterLogicalOperator:
    return cast(FilterLogicalOperator, data)
