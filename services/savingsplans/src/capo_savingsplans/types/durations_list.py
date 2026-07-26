"""Generated from Smithy shape ``com.amazonaws.savingsplans#DurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plans_duration

DurationsList: TypeAlias = list[
    "capo_savingsplans.types.savings_plans_duration.SavingsPlansDuration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DurationsList) -> list:
    return list(value)


def deserialize_json(data: list) -> DurationsList:
    return list(data)
