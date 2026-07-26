"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRatePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_rate_property

SavingsPlanRatePropertyList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_rate_property.SavingsPlanRateProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRatePropertyList) -> list:
    import capo_savingsplans.types.savings_plan_rate_property

    out: list = []
    for item in value:
        out.append(
            capo_savingsplans.types.savings_plan_rate_property.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SavingsPlanRatePropertyList:
    import capo_savingsplans.types.savings_plan_rate_property

    out: SavingsPlanRatePropertyList = []
    for item in data:
        out.append(
            capo_savingsplans.types.savings_plan_rate_property.deserialize_json(item)
        )
    return out
