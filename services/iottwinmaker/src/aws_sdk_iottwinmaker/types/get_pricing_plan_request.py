"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetPricingPlanRequest``."""

from typing_extensions import TypedDict


class GetPricingPlanRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetPricingPlanRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPricingPlanRequest:
    out: GetPricingPlanRequest = {}  # type: ignore[typeddict-item]
    return out
