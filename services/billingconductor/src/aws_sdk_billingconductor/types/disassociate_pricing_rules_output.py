"""Generated from Smithy shape ``com.amazonaws.billingconductor#DisassociatePricingRulesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_plan_arn


class DisassociatePricingRulesOutput(TypedDict):
    arn: NotRequired["aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"]
    """<p> The Amazon Resource Name (ARN) of the pricing plan that the pricing rules successfully disassociated from. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociatePricingRulesOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DisassociatePricingRulesOutput:
    out: DisassociatePricingRulesOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
