"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingRatePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_offering_rate_property

SavingsPlanOfferingRatePropertyList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_offering_rate_property.SavingsPlanOfferingRateProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingRatePropertyList) -> list:
    import capo_savingsplans.types.savings_plan_offering_rate_property

    out: list = []
    for item in value:
        out.append(
            capo_savingsplans.types.savings_plan_offering_rate_property.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SavingsPlanOfferingRatePropertyList:
    import capo_savingsplans.types.savings_plan_offering_rate_property

    out: SavingsPlanOfferingRatePropertyList = []
    for item in data:
        out.append(
            capo_savingsplans.types.savings_plan_offering_rate_property.deserialize_json(
                item
            )
        )
    return out
