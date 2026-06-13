"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListUsageFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.list_usage_filter

ListUsageFilters: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.list_usage_filter.ListUsageFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListUsageFilters) -> list:
    import aws_sdk_bcm_pricing_calculator.types.list_usage_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_usage_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListUsageFilters:
    import aws_sdk_bcm_pricing_calculator.types.list_usage_filter

    out: ListUsageFilters = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_usage_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
