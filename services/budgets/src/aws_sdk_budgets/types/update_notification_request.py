"""Generated from Smithy shape ``com.amazonaws.budgets#UpdateNotificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.notification


class UpdateNotificationRequest(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget whose notification you want to update.</p>"""
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget whose notification you want to update.</p>"""
    old_notification: "aws_sdk_budgets.types.notification.Notification"
    """<p>The previous notification that is associated with a budget.</p>"""
    new_notification: "aws_sdk_budgets.types.notification.Notification"
    """<p>The updated notification to be associated with a budget.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNotificationRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import aws_sdk_budgets.types.notification

    out["OldNotification"] = aws_sdk_budgets.types.notification.serialize_aws_json_1_1(
        value["old_notification"]
    )
    import aws_sdk_budgets.types.notification

    out["NewNotification"] = aws_sdk_budgets.types.notification.serialize_aws_json_1_1(
        value["new_notification"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNotificationRequest:
    out: UpdateNotificationRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("UpdateNotificationRequest.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("UpdateNotificationRequest.budget_name required")
    if "OldNotification" in data:
        import aws_sdk_budgets.types.notification

        out["old_notification"] = (
            aws_sdk_budgets.types.notification.deserialize_aws_json_1_1(
                data["OldNotification"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNotificationRequest.old_notification required"
        )
    if "NewNotification" in data:
        import aws_sdk_budgets.types.notification

        out["new_notification"] = (
            aws_sdk_budgets.types.notification.deserialize_aws_json_1_1(
                data["NewNotification"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNotificationRequest.new_notification required"
        )
    return out
