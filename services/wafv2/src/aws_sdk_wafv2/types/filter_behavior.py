"""Generated from Smithy shape ``com.amazonaws.wafv2#FilterBehavior``."""

from typing import Literal, TypeAlias, cast

FilterBehavior: TypeAlias = Literal[
    "KEEP",
    "DROP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterBehavior:
    return cast(FilterBehavior, data)
