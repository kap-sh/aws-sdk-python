"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanServiceCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_service_code

SavingsPlanServiceCodeList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_service_code.SavingsPlanServiceCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanServiceCodeList) -> list:
    return list(value)


def deserialize_json(data: list) -> SavingsPlanServiceCodeList:
    return list(data)
