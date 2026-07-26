"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateWorkloadEstimateUsageErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_error

BatchUpdateWorkloadEstimateUsageErrors: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_error.BatchUpdateWorkloadEstimateUsageError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateWorkloadEstimateUsageErrors) -> list:
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_error

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchUpdateWorkloadEstimateUsageErrors:
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_error

    out: BatchUpdateWorkloadEstimateUsageErrors = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
