"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AccessBudgets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.access_budget

AccessBudgets: TypeAlias = list["aws_sdk_cleanroomsml.types.access_budget.AccessBudget"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgets) -> list:
    import aws_sdk_cleanroomsml.types.access_budget

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanroomsml.types.access_budget.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessBudgets:
    import aws_sdk_cleanroomsml.types.access_budget

    out: AccessBudgets = []
    for item in data:
        out.append(aws_sdk_cleanroomsml.types.access_budget.deserialize_json(item))
    return out
