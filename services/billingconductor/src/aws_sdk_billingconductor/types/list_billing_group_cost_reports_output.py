"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupCostReportsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_cost_report_list
    import aws_sdk_billingconductor.types.token


class ListBillingGroupCostReportsOutput(TypedDict):
    billing_group_cost_reports: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_cost_report_list.BillingGroupCostReportList"
    ]
    """<p>A list of <code>BillingGroupCostReportElement</code> retrieved. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to get reports. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupCostReportsOutput) -> dict:
    out: dict = {}
    if "billing_group_cost_reports" in value:
        import aws_sdk_billingconductor.types.billing_group_cost_report_list

        out["BillingGroupCostReports"] = (
            aws_sdk_billingconductor.types.billing_group_cost_report_list.serialize_json(
                value["billing_group_cost_reports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBillingGroupCostReportsOutput:
    out: ListBillingGroupCostReportsOutput = {}  # type: ignore[typeddict-item]
    if "BillingGroupCostReports" in data:
        import aws_sdk_billingconductor.types.billing_group_cost_report_list

        out["billing_group_cost_reports"] = (
            aws_sdk_billingconductor.types.billing_group_cost_report_list.deserialize_json(
                data["BillingGroupCostReports"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
