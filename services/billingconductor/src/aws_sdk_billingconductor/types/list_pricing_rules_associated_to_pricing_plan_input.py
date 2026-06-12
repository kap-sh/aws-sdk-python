"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingRulesAssociatedToPricingPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.max_pricing_plan_results
    import aws_sdk_billingconductor.types.pricing_plan_arn
    import aws_sdk_billingconductor.types.token


class ListPricingRulesAssociatedToPricingPlanInput(TypedDict):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The billing period for which the pricing rule associations are to be listed. </p>"""
    pricing_plan_arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    """<p> The Amazon Resource Name (ARN) of the pricing plan for which associations are to be listed.</p>"""
    max_results: NotRequired[
        "aws_sdk_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
    ]
    """<p>The optional maximum number of pricing rule associations to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> The optional pagination token returned by a previous call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingRulesAssociatedToPricingPlanInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    out["PricingPlanArn"] = value["pricing_plan_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingRulesAssociatedToPricingPlanInput:
    out: ListPricingRulesAssociatedToPricingPlanInput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "PricingPlanArn" in data:
        out["pricing_plan_arn"] = data["PricingPlanArn"]
    else:
        raise DeserializationError(
            "ListPricingRulesAssociatedToPricingPlanInput.pricing_plan_arn required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
