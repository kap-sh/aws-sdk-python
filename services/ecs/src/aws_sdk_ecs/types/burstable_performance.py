"""Generated from Smithy shape ``com.amazonaws.ecs#BurstablePerformance``."""

from typing import Literal, TypeAlias, cast

BurstablePerformance: TypeAlias = Literal[
    "included",
    "required",
    "excluded",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BurstablePerformance) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BurstablePerformance:
    return cast(BurstablePerformance, data)
