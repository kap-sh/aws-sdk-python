"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AccessBudgetDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.access_budget_details

AccessBudgetDetailsList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.access_budget_details.AccessBudgetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetDetailsList) -> list:
    import aws_sdk_cleanroomsml.types.access_budget_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.access_budget_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccessBudgetDetailsList:
    import aws_sdk_cleanroomsml.types.access_budget_details

    out: AccessBudgetDetailsList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.access_budget_details.deserialize_json(item)
        )
    return out
