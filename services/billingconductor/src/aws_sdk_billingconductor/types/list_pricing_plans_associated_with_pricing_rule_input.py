"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingPlansAssociatedWithPricingRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.max_pricing_rule_results
    import aws_sdk_billingconductor.types.pricing_rule_arn
    import aws_sdk_billingconductor.types.token


class ListPricingPlansAssociatedWithPricingRuleInput(TypedDict, closed=True):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The pricing plan billing period for which associations will be listed. </p>"""
    pricing_rule_arn: "aws_sdk_billingconductor.types.pricing_rule_arn.PricingRuleArn"
    """<p> The pricing rule Amazon Resource Name (ARN) for which associations will be listed. </p>"""
    max_results: NotRequired[
        "aws_sdk_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
    ]
    """<p> The optional maximum number of pricing rule associations to retrieve. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> The optional pagination token returned by a previous call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingPlansAssociatedWithPricingRuleInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    out["PricingRuleArn"] = value["pricing_rule_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingPlansAssociatedWithPricingRuleInput:
    out: ListPricingPlansAssociatedWithPricingRuleInput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "PricingRuleArn" in data:
        out["pricing_rule_arn"] = data["PricingRuleArn"]
    else:
        raise DeserializationError(
            "ListPricingPlansAssociatedWithPricingRuleInput.pricing_rule_arn required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
