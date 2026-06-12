"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreatePricingRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_rule_arn


class CreatePricingRuleOutput(TypedDict):
    arn: NotRequired["aws_sdk_billingconductor.types.pricing_rule_arn.PricingRuleArn"]
    """<p> The Amazon Resource Name (ARN) of the created pricing rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePricingRuleOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreatePricingRuleOutput:
    out: CreatePricingRuleOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
