"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdatePricingPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.pricing_plan


class UpdatePricingPlanResponse(TypedDict, closed=True):
    current_pricing_plan: "capo_iottwinmaker.types.pricing_plan.PricingPlan"
    """<p>Update the current pricing plan.</p>"""
    pending_pricing_plan: NotRequired[
        "capo_iottwinmaker.types.pricing_plan.PricingPlan"
    ]
    """<p>Update the pending pricing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingPlanResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.pricing_plan

    out["currentPricingPlan"] = capo_iottwinmaker.types.pricing_plan.serialize_json(
        value["current_pricing_plan"]
    )
    if "pending_pricing_plan" in value:
        import capo_iottwinmaker.types.pricing_plan

        out["pendingPricingPlan"] = capo_iottwinmaker.types.pricing_plan.serialize_json(
            value["pending_pricing_plan"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePricingPlanResponse:
    out: UpdatePricingPlanResponse = {}  # type: ignore[typeddict-item]
    if "currentPricingPlan" in data:
        import capo_iottwinmaker.types.pricing_plan

        out["current_pricing_plan"] = (
            capo_iottwinmaker.types.pricing_plan.deserialize_json(
                data["currentPricingPlan"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePricingPlanResponse.current_pricing_plan required"
        )
    if "pendingPricingPlan" in data:
        import capo_iottwinmaker.types.pricing_plan

        out["pending_pricing_plan"] = (
            capo_iottwinmaker.types.pricing_plan.deserialize_json(
                data["pendingPricingPlan"]
            )
        )
    return out
