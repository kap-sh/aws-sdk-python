"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.list_billing_groups_filter
    import capo_billingconductor.types.max_billing_group_results
    import capo_billingconductor.types.token


class ListBillingGroupsInput(TypedDict, closed=True):
    billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The preferred billing period to get billing groups. </p>"""
    max_results: NotRequired[
        "capo_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
    ]
    """<p>The maximum number of billing groups to retrieve. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to get billing groups. </p>"""
    filters: NotRequired[
        "capo_billingconductor.types.list_billing_groups_filter.ListBillingGroupsFilter"
    ]
    """<p>A <code>ListBillingGroupsFilter</code> that specifies the billing group and pricing plan to retrieve billing group information. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupsInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_billingconductor.types.list_billing_groups_filter

        out["Filters"] = (
            capo_billingconductor.types.list_billing_groups_filter.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBillingGroupsInput:
    out: ListBillingGroupsInput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import capo_billingconductor.types.list_billing_groups_filter

        out["filters"] = (
            capo_billingconductor.types.list_billing_groups_filter.deserialize_json(
                data["Filters"]
            )
        )
    return out
