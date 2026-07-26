"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetActionType``."""

from typing import Literal, TypeAlias, cast

BudgetActionType: TypeAlias = Literal[
    "STOP_SCHEDULING_AND_COMPLETE_TASKS",
    "STOP_SCHEDULING_AND_CANCEL_TASKS",
]


# --- restJson1 ser/de ---
def serialize_json(value: BudgetActionType) -> str:
    return value


def deserialize_json(data: str) -> BudgetActionType:
    return cast(BudgetActionType, data)
