"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#FilterName``."""

from typing import Literal, TypeAlias, cast

FilterName: TypeAlias = Literal[
    "FEATURE",
    "SEVERITY",
    "TYPE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FilterName:
    return cast(FilterName, data)
