"""Generated from Smithy shape ``com.amazonaws.freetier#Dimension``."""

from typing import Literal, TypeAlias, cast

Dimension: TypeAlias = Literal[
    "SERVICE",
    "OPERATION",
    "USAGE_TYPE",
    "REGION",
    "FREE_TIER_TYPE",
    "DESCRIPTION",
    "USAGE_PERCENTAGE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Dimension:
    return cast(Dimension, data)
