"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociatePricingRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_plan_arn


class AssociatePricingRulesOutput(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"]
    """<p> The <code>PricingPlanArn</code> that the <code>PricingRuleArns</code> are associated with. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePricingRulesOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AssociatePricingRulesOutput:
    out: AssociatePricingRulesOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
