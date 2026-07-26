"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entry

BatchCreateWorkloadEstimateUsageEntries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entry.BatchCreateWorkloadEstimateUsageEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageEntries) -> list:
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entry

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchCreateWorkloadEstimateUsageEntries:
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entry

    out: BatchCreateWorkloadEstimateUsageEntries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
