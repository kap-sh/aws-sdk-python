"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CurrentPerformanceRisk``."""

from typing import Literal, TypeAlias, cast

CurrentPerformanceRisk: TypeAlias = Literal[
    "VeryLow",
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CurrentPerformanceRisk) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CurrentPerformanceRisk:
    return cast(CurrentPerformanceRisk, data)
