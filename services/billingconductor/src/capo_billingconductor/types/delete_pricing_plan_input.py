"""Generated from Smithy shape ``com.amazonaws.billingconductor#DeletePricingPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_plan_arn


class DeletePricingPlanInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    """<p>The Amazon Resource Name (ARN) of the pricing plan that you're deleting. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePricingPlanInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeletePricingPlanInput:
    out: DeletePricingPlanInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DeletePricingPlanInput.arn required")
    return out
