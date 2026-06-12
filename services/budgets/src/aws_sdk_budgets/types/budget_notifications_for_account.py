"""Generated from Smithy shape ``com.amazonaws.budgets#BudgetNotificationsForAccount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.notifications


class BudgetNotificationsForAccount(TypedDict):
    notifications: NotRequired["aws_sdk_budgets.types.notifications.Notifications"]
    budget_name: NotRequired["aws_sdk_budgets.types.budget_name.BudgetName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BudgetNotificationsForAccount) -> dict:
    out: dict = {}
    if "notifications" in value:
        import aws_sdk_budgets.types.notifications

        out["Notifications"] = (
            aws_sdk_budgets.types.notifications.serialize_aws_json_1_1(
                value["notifications"]
            )
        )
    if "budget_name" in value:
        out["BudgetName"] = value["budget_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BudgetNotificationsForAccount:
    out: BudgetNotificationsForAccount = {}  # type: ignore[typeddict-item]
    if "Notifications" in data:
        import aws_sdk_budgets.types.notifications

        out["notifications"] = (
            aws_sdk_budgets.types.notifications.deserialize_aws_json_1_1(
                data["Notifications"]
            )
        )
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    return out
