"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetStatus``."""

from typing import Literal, TypeAlias, cast

BudgetStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BudgetStatus) -> str:
    return value


def deserialize_json(data: str) -> BudgetStatus:
    return cast(BudgetStatus, data)
