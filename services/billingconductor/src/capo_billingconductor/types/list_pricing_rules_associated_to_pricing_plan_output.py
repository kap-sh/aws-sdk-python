"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingRulesAssociatedToPricingPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.pricing_plan_arn
    import capo_billingconductor.types.pricing_rule_arns
    import capo_billingconductor.types.token


class ListPricingRulesAssociatedToPricingPlanOutput(TypedDict, closed=True):
    billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The billing period for which the pricing rule associations are listed. </p>"""
    pricing_plan_arn: NotRequired[
        "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the pricing plan for which associations are listed.</p>"""
    pricing_rule_arns: NotRequired[
        "capo_billingconductor.types.pricing_rule_arns.PricingRuleArns"
    ]
    """<p> A list containing pricing rules that are associated with the requested pricing plan. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p> The pagination token to be used on subsequent calls. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingRulesAssociatedToPricingPlanOutput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "pricing_plan_arn" in value:
        out["PricingPlanArn"] = value["pricing_plan_arn"]
    if "pricing_rule_arns" in value:
        import capo_billingconductor.types.pricing_rule_arns

        out["PricingRuleArns"] = (
            capo_billingconductor.types.pricing_rule_arns.serialize_json(
                value["pricing_rule_arns"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingRulesAssociatedToPricingPlanOutput:
    out: ListPricingRulesAssociatedToPricingPlanOutput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "PricingPlanArn" in data:
        out["pricing_plan_arn"] = data["PricingPlanArn"]
    if "PricingRuleArns" in data:
        import capo_billingconductor.types.pricing_rule_arns

        out["pricing_rule_arns"] = (
            capo_billingconductor.types.pricing_rule_arns.deserialize_json(
                data["PricingRuleArns"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
