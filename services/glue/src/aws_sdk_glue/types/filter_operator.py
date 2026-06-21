"""Generated from Smithy shape ``com.amazonaws.glue#FilterOperator``."""

from typing import Literal, TypeAlias, cast

FilterOperator: TypeAlias = Literal[
    "GT",
    "GE",
    "LT",
    "LE",
    "EQ",
    "NE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterOperator:
    return cast(FilterOperator, data)
