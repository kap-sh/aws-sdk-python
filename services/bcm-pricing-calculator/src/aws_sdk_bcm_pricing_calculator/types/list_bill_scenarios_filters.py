"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillScenariosFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filter

ListBillScenariosFilters: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filter.ListBillScenariosFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillScenariosFilters) -> list:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListBillScenariosFilters:
    import aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filter

    out: ListBillScenariosFilters = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
