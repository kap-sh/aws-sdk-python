"""Generated from Smithy shape ``com.amazonaws.glue#FilterOperation``."""

from typing import Literal, TypeAlias, cast

FilterOperation: TypeAlias = Literal[
    "EQ",
    "LT",
    "GT",
    "LTE",
    "GTE",
    "REGEX",
    "ISNULL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterOperation:
    return cast(FilterOperation, data)
