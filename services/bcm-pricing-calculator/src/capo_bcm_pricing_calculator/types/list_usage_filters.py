"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListUsageFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.list_usage_filter

ListUsageFilters: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.list_usage_filter.ListUsageFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListUsageFilters) -> list:
    import capo_bcm_pricing_calculator.types.list_usage_filter

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.list_usage_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListUsageFilters:
    import capo_bcm_pricing_calculator.types.list_usage_filter

    out: ListUsageFilters = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.list_usage_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
