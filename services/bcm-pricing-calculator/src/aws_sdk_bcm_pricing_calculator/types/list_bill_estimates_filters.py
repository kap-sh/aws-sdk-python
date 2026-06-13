"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimatesFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter

ListBillEstimatesFilters: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter.ListBillEstimatesFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillEstimatesFilters) -> list:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListBillEstimatesFilters:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter

    out: ListBillEstimatesFilters = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
