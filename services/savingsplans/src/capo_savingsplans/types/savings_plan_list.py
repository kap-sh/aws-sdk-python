"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan

SavingsPlanList: TypeAlias = list["capo_savingsplans.types.savings_plan.SavingsPlan"]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanList) -> list:
    import capo_savingsplans.types.savings_plan

    out: list = []
    for item in value:
        out.append(capo_savingsplans.types.savings_plan.serialize_json(item))
    return out


def deserialize_json(data: list) -> SavingsPlanList:
    import capo_savingsplans.types.savings_plan

    out: SavingsPlanList = []
    for item in data:
        out.append(capo_savingsplans.types.savings_plan.deserialize_json(item))
    return out
