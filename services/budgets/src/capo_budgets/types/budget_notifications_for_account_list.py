"""Generated from Smithy shape ``com.amazonaws.budgets#BudgetNotificationsForAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.budget_notifications_for_account

BudgetNotificationsForAccountList: TypeAlias = list[
    "capo_budgets.types.budget_notifications_for_account.BudgetNotificationsForAccount"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BudgetNotificationsForAccountList) -> list:
    import capo_budgets.types.budget_notifications_for_account

    out: list = []
    for item in value:
        out.append(
            capo_budgets.types.budget_notifications_for_account.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BudgetNotificationsForAccountList:
    import capo_budgets.types.budget_notifications_for_account

    out: BudgetNotificationsForAccountList = []
    for item in data:
        out.append(
            capo_budgets.types.budget_notifications_for_account.deserialize_aws_json_1_1(
                item
            )
        )
    return out
