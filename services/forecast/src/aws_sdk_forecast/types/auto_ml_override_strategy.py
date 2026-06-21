"""Generated from Smithy shape ``com.amazonaws.forecast#AutoMLOverrideStrategy``."""

from typing import Literal, TypeAlias, cast

AutoMLOverrideStrategy: TypeAlias = Literal[
    "LatencyOptimized",
    "AccuracyOptimized",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLOverrideStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLOverrideStrategy:
    return cast(AutoMLOverrideStrategy, data)
