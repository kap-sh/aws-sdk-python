"""Generated from Smithy shape ``com.amazonaws.forecast#FilterConditionString``."""

from typing import Literal, TypeAlias, cast

FilterConditionString: TypeAlias = Literal[
    "IS",
    "IS_NOT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterConditionString) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterConditionString:
    return cast(FilterConditionString, data)
