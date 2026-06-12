"""Generated from Smithy shape ``com.amazonaws.deadline#DefaultQueueBudgetAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

DefaultQueueBudgetAction: TypeAlias = Literal[
    "NONE",
    "STOP_SCHEDULING_AND_COMPLETE_TASKS",
    "STOP_SCHEDULING_AND_CANCEL_TASKS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "STOP_SCHEDULING_AND_COMPLETE_TASKS",
        "STOP_SCHEDULING_AND_CANCEL_TASKS",
    )
)


def serialize_json(value: DefaultQueueBudgetAction) -> str:
    return value


def deserialize_json(data: str) -> DefaultQueueBudgetAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefaultQueueBudgetAction value: {data!r}")
    return cast(DefaultQueueBudgetAction, data)
