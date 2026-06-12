"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetActionsToAdd``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.budget_action_to_add

BudgetActionsToAdd: TypeAlias = list[
    "aws_sdk_deadline.types.budget_action_to_add.BudgetActionToAdd"
]


# --- restJson1 ser/de ---
def serialize_json(value: BudgetActionsToAdd) -> list:
    import aws_sdk_deadline.types.budget_action_to_add

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.budget_action_to_add.serialize_json(item))
    return out


def deserialize_json(data: list) -> BudgetActionsToAdd:
    import aws_sdk_deadline.types.budget_action_to_add

    out: BudgetActionsToAdd = []
    for item in data:
        out.append(aws_sdk_deadline.types.budget_action_to_add.deserialize_json(item))
    return out
