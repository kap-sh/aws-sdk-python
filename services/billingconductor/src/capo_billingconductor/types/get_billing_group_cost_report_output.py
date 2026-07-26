"""Generated from Smithy shape ``com.amazonaws.billingconductor#GetBillingGroupCostReportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_cost_report_results_list
    import capo_billingconductor.types.token


class GetBillingGroupCostReportOutput(TypedDict, closed=True):
    billing_group_cost_report_results: NotRequired[
        "capo_billingconductor.types.billing_group_cost_report_results_list.BillingGroupCostReportResultsList"
    ]
    """<p>The list of margin summary reports.</p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p>The pagination token used on subsequent calls to get reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBillingGroupCostReportOutput) -> dict:
    out: dict = {}
    if "billing_group_cost_report_results" in value:
        import capo_billingconductor.types.billing_group_cost_report_results_list

        out["BillingGroupCostReportResults"] = (
            capo_billingconductor.types.billing_group_cost_report_results_list.serialize_json(
                value["billing_group_cost_report_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBillingGroupCostReportOutput:
    out: GetBillingGroupCostReportOutput = {}  # type: ignore[typeddict-item]
    if "BillingGroupCostReportResults" in data:
        import capo_billingconductor.types.billing_group_cost_report_results_list

        out["billing_group_cost_report_results"] = (
            capo_billingconductor.types.billing_group_cost_report_results_list.deserialize_json(
                data["BillingGroupCostReportResults"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
