"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BudgetParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.budget_parameter

BudgetParameters: TypeAlias = list[
    "capo_cleanrooms.types.budget_parameter.BudgetParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: BudgetParameters) -> list:
    import capo_cleanrooms.types.budget_parameter

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.budget_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> BudgetParameters:
    import capo_cleanrooms.types.budget_parameter

    out: BudgetParameters = []
    for item in data:
        out.append(capo_cleanrooms.types.budget_parameter.deserialize_json(item))
    return out
