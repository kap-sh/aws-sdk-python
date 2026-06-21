"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ImplementationEffort``."""

from typing import Literal, TypeAlias, cast

ImplementationEffort: TypeAlias = Literal[
    "VeryLow",
    "Low",
    "Medium",
    "High",
    "VeryHigh",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImplementationEffort) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ImplementationEffort:
    return cast(ImplementationEffort, data)
