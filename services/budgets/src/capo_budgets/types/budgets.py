"""Generated from Smithy shape ``com.amazonaws.budgets#Budgets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.budget

Budgets: TypeAlias = list["capo_budgets.types.budget.Budget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Budgets) -> list:
    import capo_budgets.types.budget

    out: list = []
    for item in value:
        out.append(capo_budgets.types.budget.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Budgets:
    import capo_budgets.types.budget

    out: Budgets = []
    for item in data:
        out.append(capo_budgets.types.budget.deserialize_aws_json_1_1(item))
    return out
