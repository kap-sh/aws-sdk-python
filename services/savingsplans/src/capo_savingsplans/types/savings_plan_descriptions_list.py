"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanDescriptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_description

SavingsPlanDescriptionsList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_description.SavingsPlanDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanDescriptionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> SavingsPlanDescriptionsList:
    return list(data)
