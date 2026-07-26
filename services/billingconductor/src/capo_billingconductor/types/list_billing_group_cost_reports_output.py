"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupCostReportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_cost_report_list
    import capo_billingconductor.types.token


class ListBillingGroupCostReportsOutput(TypedDict, closed=True):
    billing_group_cost_reports: NotRequired[
        "capo_billingconductor.types.billing_group_cost_report_list.BillingGroupCostReportList"
    ]
    """<p>A list of <code>BillingGroupCostReportElement</code> retrieved. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to get reports. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupCostReportsOutput) -> dict:
    out: dict = {}
    if "billing_group_cost_reports" in value:
        import capo_billingconductor.types.billing_group_cost_report_list

        out["BillingGroupCostReports"] = (
            capo_billingconductor.types.billing_group_cost_report_list.serialize_json(
                value["billing_group_cost_reports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBillingGroupCostReportsOutput:
    out: ListBillingGroupCostReportsOutput = {}  # type: ignore[typeddict-item]
    if "BillingGroupCostReports" in data:
        import capo_billingconductor.types.billing_group_cost_report_list

        out["billing_group_cost_reports"] = (
            capo_billingconductor.types.billing_group_cost_report_list.deserialize_json(
                data["BillingGroupCostReports"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
