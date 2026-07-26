"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateUsageItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.workload_estimate_usage_item

WorkloadEstimateUsageItems: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.workload_estimate_usage_item.WorkloadEstimateUsageItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateUsageItems) -> list:
    import capo_bcm_pricing_calculator.types.workload_estimate_usage_item

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.workload_estimate_usage_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> WorkloadEstimateUsageItems:
    import capo_bcm_pricing_calculator.types.workload_estimate_usage_item

    out: WorkloadEstimateUsageItems = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.workload_estimate_usage_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
