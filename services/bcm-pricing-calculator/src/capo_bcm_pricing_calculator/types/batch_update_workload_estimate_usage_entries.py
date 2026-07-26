"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateWorkloadEstimateUsageEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entry

BatchUpdateWorkloadEstimateUsageEntries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entry.BatchUpdateWorkloadEstimateUsageEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateWorkloadEstimateUsageEntries) -> list:
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entry

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchUpdateWorkloadEstimateUsageEntries:
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entry

    out: BatchUpdateWorkloadEstimateUsageEntries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
