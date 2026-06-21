"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#MetricName``."""

from typing import Literal, TypeAlias, cast

MetricName: TypeAlias = Literal[
    "AmortizedCost",
    "BlendedCost",
    "NetAmortizedCost",
    "NetUnblendedCost",
    "NormalizedUsageAmount",
    "UnblendedCost",
    "UsageQuantity",
    "SpendCoveredBySavingsPlans",
    "Hour",
    "Unit",
    "Cost",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricName:
    return cast(MetricName, data)
