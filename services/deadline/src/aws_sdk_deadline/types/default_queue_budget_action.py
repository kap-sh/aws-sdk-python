"""Generated from Smithy shape ``com.amazonaws.deadline#DefaultQueueBudgetAction``."""

from typing import Literal, TypeAlias, cast

DefaultQueueBudgetAction: TypeAlias = Literal[
    "NONE",
    "STOP_SCHEDULING_AND_COMPLETE_TASKS",
    "STOP_SCHEDULING_AND_CANCEL_TASKS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultQueueBudgetAction) -> str:
    return value


def deserialize_json(data: str) -> DefaultQueueBudgetAction:
    return cast(DefaultQueueBudgetAction, data)
