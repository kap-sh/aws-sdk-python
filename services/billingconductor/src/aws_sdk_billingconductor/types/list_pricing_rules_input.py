"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.list_pricing_rules_filter
    import aws_sdk_billingconductor.types.max_pricing_rule_results
    import aws_sdk_billingconductor.types.token


class ListPricingRulesInput(TypedDict, closed=True):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The preferred billing period to get the pricing plan. </p>"""
    filters: NotRequired[
        "aws_sdk_billingconductor.types.list_pricing_rules_filter.ListPricingRulesFilter"
    ]
    """<p> A <code>DescribePricingRuleFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing rules to retrieve pricing rules information. </p>"""
    max_results: NotRequired[
        "aws_sdk_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
    ]
    """<p> The maximum number of pricing rules to retrieve. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent call to get pricing rules. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingRulesInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "filters" in value:
        import aws_sdk_billingconductor.types.list_pricing_rules_filter

        out["Filters"] = (
            aws_sdk_billingconductor.types.list_pricing_rules_filter.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingRulesInput:
    out: ListPricingRulesInput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "Filters" in data:
        import aws_sdk_billingconductor.types.list_pricing_rules_filter

        out["filters"] = (
            aws_sdk_billingconductor.types.list_pricing_rules_filter.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
