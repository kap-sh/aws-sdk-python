"""Generated from Smithy shape ``com.amazonaws.billingconductor#DeletePricingPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_plan_arn


class DeletePricingPlanOutput(TypedDict, closed=True):
    arn: NotRequired["capo_billingconductor.types.pricing_plan_arn.PricingPlanArn"]
    """<p> The Amazon Resource Name (ARN) of the deleted pricing plan. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePricingPlanOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeletePricingPlanOutput:
    out: DeletePricingPlanOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
