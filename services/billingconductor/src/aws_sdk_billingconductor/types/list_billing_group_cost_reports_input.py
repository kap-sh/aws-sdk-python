"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupCostReportsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.list_billing_group_cost_reports_filter
    import aws_sdk_billingconductor.types.max_billing_group_results
    import aws_sdk_billingconductor.types.token


class ListBillingGroupCostReportsInput(TypedDict):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The preferred billing period for your report. </p>"""
    max_results: NotRequired[
        "aws_sdk_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
    ]
    """<p>The maximum number of reports to retrieve. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to get reports. </p>"""
    filters: NotRequired[
        "aws_sdk_billingconductor.types.list_billing_group_cost_reports_filter.ListBillingGroupCostReportsFilter"
    ]
    """<p>A <code>ListBillingGroupCostReportsFilter</code> to specify billing groups to retrieve reports from. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupCostReportsInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_billingconductor.types.list_billing_group_cost_reports_filter

        out["Filters"] = (
            aws_sdk_billingconductor.types.list_billing_group_cost_reports_filter.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBillingGroupCostReportsInput:
    out: ListBillingGroupCostReportsInput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_billingconductor.types.list_billing_group_cost_reports_filter

        out["filters"] = (
            aws_sdk_billingconductor.types.list_billing_group_cost_reports_filter.deserialize_json(
                data["Filters"]
            )
        )
    return out
