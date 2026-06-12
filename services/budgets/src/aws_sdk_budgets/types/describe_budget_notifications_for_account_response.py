"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetNotificationsForAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_budgets.types.budget_notifications_for_account_list
    import aws_sdk_budgets.types.generic_string


class DescribeBudgetNotificationsForAccountResponse(TypedDict):
    budget_notifications_for_account: NotRequired[
        "aws_sdk_budgets.types.budget_notifications_for_account_list.BudgetNotificationsForAccountList"
    ]
    """<p> A list of budget names and associated notifications for an account. </p>"""
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeBudgetNotificationsForAccountResponse,
) -> dict:
    out: dict = {}
    if "budget_notifications_for_account" in value:
        import aws_sdk_budgets.types.budget_notifications_for_account_list

        out["BudgetNotificationsForAccount"] = (
            aws_sdk_budgets.types.budget_notifications_for_account_list.serialize_aws_json_1_1(
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
        import aws_sdk_budgets.types.budget_notifications_for_account_list

        out["budget_notifications_for_account"] = (
            aws_sdk_budgets.types.budget_notifications_for_account_list.deserialize_aws_json_1_1(
                data["BudgetNotificationsForAccount"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
