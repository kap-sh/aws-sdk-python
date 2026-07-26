"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteWorkloadEstimateUsageErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_error

BatchDeleteWorkloadEstimateUsageErrors: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_error.BatchDeleteWorkloadEstimateUsageError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchDeleteWorkloadEstimateUsageErrors) -> list:
    import capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_error

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchDeleteWorkloadEstimateUsageErrors:
    import capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_error

    out: BatchDeleteWorkloadEstimateUsageErrors = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
