"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_rate_operation

SavingsPlanRateOperationList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_rate_operation.SavingsPlanRateOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateOperationList) -> list:
    return list(value)


def deserialize_json(data: list) -> SavingsPlanRateOperationList:
    return list(data)
