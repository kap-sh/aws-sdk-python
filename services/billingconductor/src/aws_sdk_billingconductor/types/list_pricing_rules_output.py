"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingRulesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.pricing_rule_list
    import aws_sdk_billingconductor.types.token


class ListPricingRulesOutput(TypedDict):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The billing period for which the described pricing rules are applicable. </p>"""
    pricing_rules: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_list.PricingRuleList"
    ]
    """<p> A list containing the described pricing rules. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent calls to get pricing rules. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingRulesOutput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "pricing_rules" in value:
        import aws_sdk_billingconductor.types.pricing_rule_list

        out["PricingRules"] = (
            aws_sdk_billingconductor.types.pricing_rule_list.serialize_json(
                value["pricing_rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingRulesOutput:
    out: ListPricingRulesOutput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "PricingRules" in data:
        import aws_sdk_billingconductor.types.pricing_rule_list

        out["pricing_rules"] = (
            aws_sdk_billingconductor.types.pricing_rule_list.deserialize_json(
                data["PricingRules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
