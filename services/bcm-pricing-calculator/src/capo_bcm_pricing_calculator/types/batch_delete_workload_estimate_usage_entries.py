"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteWorkloadEstimateUsageEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.resource_id

BatchDeleteWorkloadEstimateUsageEntries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchDeleteWorkloadEstimateUsageEntries) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BatchDeleteWorkloadEstimateUsageEntries:
    return list(data)
