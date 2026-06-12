"""Generated from Smithy shape ``com.amazonaws.billingconductor#DeletePricingRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_rule_arn


class DeletePricingRuleInput(TypedDict):
    arn: "aws_sdk_billingconductor.types.pricing_rule_arn.PricingRuleArn"
    """<p> The Amazon Resource Name (ARN) of the pricing rule that you are deleting. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePricingRuleInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeletePricingRuleInput:
    out: DeletePricingRuleInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DeletePricingRuleInput.arn required")
    return out
