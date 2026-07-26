"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanUsageTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_usage_type

SavingsPlanUsageTypeList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_usage_type.SavingsPlanUsageType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanUsageTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> SavingsPlanUsageTypeList:
    return list(data)
