"""Generated from Smithy shape ``com.amazonaws.wafv2#FilterRequirement``."""

from typing import Literal, TypeAlias, cast

FilterRequirement: TypeAlias = Literal[
    "MEETS_ALL",
    "MEETS_ANY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterRequirement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterRequirement:
    return cast(FilterRequirement, data)
