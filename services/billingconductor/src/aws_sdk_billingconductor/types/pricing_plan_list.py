"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingPlanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_plan_list_element

PricingPlanList: TypeAlias = list[
    "aws_sdk_billingconductor.types.pricing_plan_list_element.PricingPlanListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingPlanList) -> list:
    import aws_sdk_billingconductor.types.pricing_plan_list_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.pricing_plan_list_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PricingPlanList:
    import aws_sdk_billingconductor.types.pricing_plan_list_element

    out: PricingPlanList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.pricing_plan_list_element.deserialize_json(
                item
            )
        )
    return out
