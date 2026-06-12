"""Generated from Smithy shape ``com.amazonaws.billingconductor#GetBillingGroupCostReportOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_cost_report_results_list
    import aws_sdk_billingconductor.types.token


class GetBillingGroupCostReportOutput(TypedDict):
    billing_group_cost_report_results: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_cost_report_results_list.BillingGroupCostReportResultsList"
    ]
    """<p>The list of margin summary reports.</p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p>The pagination token used on subsequent calls to get reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBillingGroupCostReportOutput) -> dict:
    out: dict = {}
    if "billing_group_cost_report_results" in value:
        import aws_sdk_billingconductor.types.billing_group_cost_report_results_list

        out["BillingGroupCostReportResults"] = (
            aws_sdk_billingconductor.types.billing_group_cost_report_results_list.serialize_json(
                value["billing_group_cost_report_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBillingGroupCostReportOutput:
    out: GetBillingGroupCostReportOutput = {}  # type: ignore[typeddict-item]
    if "BillingGroupCostReportResults" in data:
        import aws_sdk_billingconductor.types.billing_group_cost_report_results_list

        out["billing_group_cost_report_results"] = (
            aws_sdk_billingconductor.types.billing_group_cost_report_results_list.deserialize_json(
                data["BillingGroupCostReportResults"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
