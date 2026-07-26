"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetActionsToRemove``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.budget_action_to_remove

BudgetActionsToRemove: TypeAlias = list[
    "capo_deadline.types.budget_action_to_remove.BudgetActionToRemove"
]


# --- restJson1 ser/de ---
def serialize_json(value: BudgetActionsToRemove) -> list:
    import capo_deadline.types.budget_action_to_remove

    out: list = []
    for item in value:
        out.append(capo_deadline.types.budget_action_to_remove.serialize_json(item))
    return out


def deserialize_json(data: list) -> BudgetActionsToRemove:
    import capo_deadline.types.budget_action_to_remove

    out: BudgetActionsToRemove = []
    for item in data:
        out.append(capo_deadline.types.budget_action_to_remove.deserialize_json(item))
    return out
