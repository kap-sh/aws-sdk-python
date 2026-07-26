"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_id

SavingsPlanIdList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_id.SavingsPlanId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SavingsPlanIdList:
    return list(data)
