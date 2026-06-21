"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AccessBudgetType``."""

from typing import Literal, TypeAlias, cast

AccessBudgetType: TypeAlias = Literal[
    "CALENDAR_DAY",
    "CALENDAR_MONTH",
    "CALENDAR_WEEK",
    "LIFETIME",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetType) -> str:
    return value


def deserialize_json(data: str) -> AccessBudgetType:
    return cast(AccessBudgetType, data)
