"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_item

BatchCreateWorkloadEstimateUsageItems: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_item.BatchCreateWorkloadEstimateUsageItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageItems) -> list:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchCreateWorkloadEstimateUsageItems:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_item

    out: BatchCreateWorkloadEstimateUsageItems = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
