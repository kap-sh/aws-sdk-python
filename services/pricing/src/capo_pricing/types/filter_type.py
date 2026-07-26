"""Generated from Smithy shape ``com.amazonaws.pricing#FilterType``."""

from typing import Literal, TypeAlias, cast

FilterType: TypeAlias = Literal[
    "TERM_MATCH",
    "EQUALS",
    "CONTAINS",
    "ANY_OF",
    "NONE_OF",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterType:
    return cast(FilterType, data)
