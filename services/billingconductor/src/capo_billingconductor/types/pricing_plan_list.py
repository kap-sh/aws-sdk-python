"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingPlanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_plan_list_element

PricingPlanList: TypeAlias = list[
    "capo_billingconductor.types.pricing_plan_list_element.PricingPlanListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingPlanList) -> list:
    import capo_billingconductor.types.pricing_plan_list_element

    out: list = []
    for item in value:
        out.append(
            capo_billingconductor.types.pricing_plan_list_element.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PricingPlanList:
    import capo_billingconductor.types.pricing_plan_list_element

    out: PricingPlanList = []
    for item in data:
        out.append(
            capo_billingconductor.types.pricing_plan_list_element.deserialize_json(item)
        )
    return out
