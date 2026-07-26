"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_arn

SavingsPlanArnList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_arn.SavingsPlanArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> SavingsPlanArnList:
    return list(data)
