"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#MetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_dashboards.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_0(value: MetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricName value: {data!r}")
    return cast(MetricName, data)
