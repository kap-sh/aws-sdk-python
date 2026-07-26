"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_rate

SavingsPlanRateList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_rate.SavingsPlanRate"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateList) -> list:
    import capo_savingsplans.types.savings_plan_rate

    out: list = []
    for item in value:
        out.append(capo_savingsplans.types.savings_plan_rate.serialize_json(item))
    return out


def deserialize_json(data: list) -> SavingsPlanRateList:
    import capo_savingsplans.types.savings_plan_rate

    out: SavingsPlanRateList = []
    for item in data:
        out.append(capo_savingsplans.types.savings_plan_rate.deserialize_json(item))
    return out
