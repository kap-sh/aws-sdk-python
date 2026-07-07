"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreatePricingPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_plan_arn


class CreatePricingPlanOutput(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"]
    """<p>The Amazon Resource Name (ARN) of the created pricing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePricingPlanOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreatePricingPlanOutput:
    out: CreatePricingPlanOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
