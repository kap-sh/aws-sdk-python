"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListWorkloadEstimatesFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_filter

ListWorkloadEstimatesFilters: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_filter.ListWorkloadEstimatesFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkloadEstimatesFilters) -> list:
    import aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListWorkloadEstimatesFilters:
    import aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_filter

    out: ListWorkloadEstimatesFilters = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
