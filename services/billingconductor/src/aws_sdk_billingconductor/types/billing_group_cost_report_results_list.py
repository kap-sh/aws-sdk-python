"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupCostReportResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_cost_report_result_element

BillingGroupCostReportResultsList: TypeAlias = list[
    "aws_sdk_billingconductor.types.billing_group_cost_report_result_element.BillingGroupCostReportResultElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupCostReportResultsList) -> list:
    import aws_sdk_billingconductor.types.billing_group_cost_report_result_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.billing_group_cost_report_result_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BillingGroupCostReportResultsList:
    import aws_sdk_billingconductor.types.billing_group_cost_report_result_element

    out: BillingGroupCostReportResultsList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.billing_group_cost_report_result_element.deserialize_json(
                item
            )
        )
    return out
