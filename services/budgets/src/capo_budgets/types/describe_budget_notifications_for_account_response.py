"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetNotificationsForAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.budget_notifications_for_account_list
    import capo_budgets.types.generic_string


class DescribeBudgetNotificationsForAccountResponse(TypedDict, closed=True):
    budget_notifications_for_account: NotRequired[
        "capo_budgets.types.budget_notifications_for_account_list.BudgetNotificationsForAccountList"
    ]
    """<p> A list of budget names and associated notifications for an account. </p>"""
    next_token: NotRequired["capo_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeBudgetNotificationsForAccountResponse,
) -> dict:
    out: dict = {}
    if "budget_notifications_for_account" in value:
        import capo_budgets.types.budget_notifications_for_account_list

        out["BudgetNotificationsForAccount"] = (
            capo_budgets.types.budget_notifications_for_account_list.serialize_aws_json_1_1(
                value["budget_notifications_for_account"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeBudgetNotificationsForAccountResponse:
    out: DescribeBudgetNotificationsForAccountResponse = {}  # type: ignore[typeddict-item]
    if "BudgetNotificationsForAccount" in data:
        import capo_budgets.types.budget_notifications_for_account_list

        out["budget_notifications_for_account"] = (
            capo_budgets.types.budget_notifications_for_account_list.deserialize_aws_json_1_1(
                data["BudgetNotificationsForAccount"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
