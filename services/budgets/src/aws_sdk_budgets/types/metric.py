"""Generated from Smithy shape ``com.amazonaws.budgets#Metric``."""

from typing import Literal, TypeAlias, cast

Metric: TypeAlias = Literal[
    "BlendedCost",
    "UnblendedCost",
    "AmortizedCost",
    "NetUnblendedCost",
    "NetAmortizedCost",
    "UsageQuantity",
    "NormalizedUsageAmount",
    "Hours",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Metric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Metric:
    return cast(Metric, data)
