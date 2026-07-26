"""Generated from Smithy shape ``com.amazonaws.budgets#BudgetedAndActualAmountsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.budgeted_and_actual_amounts

BudgetedAndActualAmountsList: TypeAlias = list[
    "capo_budgets.types.budgeted_and_actual_amounts.BudgetedAndActualAmounts"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BudgetedAndActualAmountsList) -> list:
    import capo_budgets.types.budgeted_and_actual_amounts

    out: list = []
    for item in value:
        out.append(
            capo_budgets.types.budgeted_and_actual_amounts.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BudgetedAndActualAmountsList:
    import capo_budgets.types.budgeted_and_actual_amounts

    out: BudgetedAndActualAmountsList = []
    for item in data:
        out.append(
            capo_budgets.types.budgeted_and_actual_amounts.deserialize_aws_json_1_1(
                item
            )
        )
    return out
