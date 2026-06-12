"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingPlansInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.list_pricing_plans_filter
    import aws_sdk_billingconductor.types.max_pricing_plan_results
    import aws_sdk_billingconductor.types.token


class ListPricingPlansInput(TypedDict):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The preferred billing period to get pricing plan. </p>"""
    filters: NotRequired[
        "aws_sdk_billingconductor.types.list_pricing_plans_filter.ListPricingPlansFilter"
    ]
    """<p>A <code>ListPricingPlansFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing plans to retrieve pricing plans information.</p>"""
    max_results: NotRequired[
        "aws_sdk_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
    ]
    """<p>The maximum number of pricing plans to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent call to get pricing plans. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingPlansInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "filters" in value:
        import aws_sdk_billingconductor.types.list_pricing_plans_filter

        out["Filters"] = (
            aws_sdk_billingconductor.types.list_pricing_plans_filter.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingPlansInput:
    out: ListPricingPlansInput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "Filters" in data:
        import aws_sdk_billingconductor.types.list_pricing_plans_filter

        out["filters"] = (
            aws_sdk_billingconductor.types.list_pricing_plans_filter.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
