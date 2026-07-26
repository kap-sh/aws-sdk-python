"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudgetDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.access_budget_details

AccessBudgetDetailsList: TypeAlias = list[
    "capo_cleanrooms.types.access_budget_details.AccessBudgetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetDetailsList) -> list:
    import capo_cleanrooms.types.access_budget_details

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.access_budget_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessBudgetDetailsList:
    import capo_cleanrooms.types.access_budget_details

    out: AccessBudgetDetailsList = []
    for item in data:
        out.append(capo_cleanrooms.types.access_budget_details.deserialize_json(item))
    return out
