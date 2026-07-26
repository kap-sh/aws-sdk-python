"""Generated from Smithy shape ``com.amazonaws.billingconductor#DeletePricingRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_rule_arn


class DeletePricingRuleOutput(TypedDict, closed=True):
    arn: NotRequired["capo_billingconductor.types.pricing_rule_arn.PricingRuleArn"]
    """<p> The Amazon Resource Name (ARN) of the deleted pricing rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePricingRuleOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeletePricingRuleOutput:
    out: DeletePricingRuleOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
