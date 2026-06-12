"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BudgetActionType: TypeAlias = Literal[
    "STOP_SCHEDULING_AND_COMPLETE_TASKS",
    "STOP_SCHEDULING_AND_CANCEL_TASKS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STOP_SCHEDULING_AND_COMPLETE_TASKS",
        "STOP_SCHEDULING_AND_CANCEL_TASKS",
    )
)


def serialize_json(value: BudgetActionType) -> str:
    return value


def deserialize_json(data: str) -> BudgetActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BudgetActionType value: {data!r}")
    return cast(BudgetActionType, data)
