"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimateLineItemsFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter

ListBillEstimateLineItemsFilters: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter.ListBillEstimateLineItemsFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillEstimateLineItemsFilters) -> list:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListBillEstimateLineItemsFilters:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter

    out: ListBillEstimateLineItemsFilters = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
