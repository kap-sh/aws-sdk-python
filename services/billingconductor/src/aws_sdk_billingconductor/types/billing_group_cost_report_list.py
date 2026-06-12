"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupCostReportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_cost_report_element

BillingGroupCostReportList: TypeAlias = list[
    "aws_sdk_billingconductor.types.billing_group_cost_report_element.BillingGroupCostReportElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupCostReportList) -> list:
    import aws_sdk_billingconductor.types.billing_group_cost_report_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.billing_group_cost_report_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BillingGroupCostReportList:
    import aws_sdk_billingconductor.types.billing_group_cost_report_element

    out: BillingGroupCostReportList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.billing_group_cost_report_element.deserialize_json(
                item
            )
        )
    return out
