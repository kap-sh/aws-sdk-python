"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociatePricingRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_plan_arn
    import aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input


class AssociatePricingRulesInput(TypedDict, closed=True):
    arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    """<p> The <code>PricingPlanArn</code> that the <code>PricingRuleArns</code> are associated with. </p>"""
    pricing_rule_arns: "aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput"
    """<p> The <code>PricingRuleArns</code> that are associated with the Pricing Plan. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePricingRulesInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input

    out["PricingRuleArns"] = (
        aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input.serialize_json(
            value["pricing_rule_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssociatePricingRulesInput:
    out: AssociatePricingRulesInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("AssociatePricingRulesInput.arn required")
    if "PricingRuleArns" in data:
        import aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input

        out["pricing_rule_arns"] = (
            aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input.deserialize_json(
                data["PricingRuleArns"]
            )
        )
    else:
        raise DeserializationError(
            "AssociatePricingRulesInput.pricing_rule_arns required"
        )
    return out
