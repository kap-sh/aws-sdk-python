"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetPricingPlanResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.pricing_plan


class GetPricingPlanResponse(TypedDict):
    current_pricing_plan: "aws_sdk_iottwinmaker.types.pricing_plan.PricingPlan"
    """<p>The chosen pricing plan for the current billing cycle.</p>"""
    pending_pricing_plan: NotRequired[
        "aws_sdk_iottwinmaker.types.pricing_plan.PricingPlan"
    ]
    """<p>The pending pricing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPricingPlanResponse) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.pricing_plan

    out["currentPricingPlan"] = aws_sdk_iottwinmaker.types.pricing_plan.serialize_json(
        value["current_pricing_plan"]
    )
    if "pending_pricing_plan" in value:
        import aws_sdk_iottwinmaker.types.pricing_plan

        out["pendingPricingPlan"] = (
            aws_sdk_iottwinmaker.types.pricing_plan.serialize_json(
                value["pending_pricing_plan"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPricingPlanResponse:
    out: GetPricingPlanResponse = {}  # type: ignore[typeddict-item]
    if "currentPricingPlan" in data:
        import aws_sdk_iottwinmaker.types.pricing_plan

        out["current_pricing_plan"] = (
            aws_sdk_iottwinmaker.types.pricing_plan.deserialize_json(
                data["currentPricingPlan"]
            )
        )
    else:
        raise DeserializationError(
            "GetPricingPlanResponse.current_pricing_plan required"
        )
    if "pendingPricingPlan" in data:
        import aws_sdk_iottwinmaker.types.pricing_plan

        out["pending_pricing_plan"] = (
            aws_sdk_iottwinmaker.types.pricing_plan.deserialize_json(
                data["pendingPricingPlan"]
            )
        )
    return out
