"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingPlansAssociatedWithPricingRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.pricing_plan_arns
    import aws_sdk_billingconductor.types.pricing_rule_arn
    import aws_sdk_billingconductor.types.token


class ListPricingPlansAssociatedWithPricingRuleOutput(TypedDict):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The pricing plan billing period for which associations will be listed. </p>"""
    pricing_rule_arn: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_arn.PricingRuleArn"
    ]
    """<p> The pricing rule Amazon Resource Name (ARN) for which associations will be listed. </p>"""
    pricing_plan_arns: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_arns.PricingPlanArns"
    ]
    """<p> The list containing pricing plans that are associated with the requested pricing rule. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> The pagination token to be used on subsequent calls. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingPlansAssociatedWithPricingRuleOutput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "pricing_rule_arn" in value:
        out["PricingRuleArn"] = value["pricing_rule_arn"]
    if "pricing_plan_arns" in value:
        import aws_sdk_billingconductor.types.pricing_plan_arns

        out["PricingPlanArns"] = (
            aws_sdk_billingconductor.types.pricing_plan_arns.serialize_json(
                value["pricing_plan_arns"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingPlansAssociatedWithPricingRuleOutput:
    out: ListPricingPlansAssociatedWithPricingRuleOutput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "PricingRuleArn" in data:
        out["pricing_rule_arn"] = data["PricingRuleArn"]
    if "PricingPlanArns" in data:
        import aws_sdk_billingconductor.types.pricing_plan_arns

        out["pricing_plan_arns"] = (
            aws_sdk_billingconductor.types.pricing_plan_arns.deserialize_json(
                data["PricingPlanArns"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
