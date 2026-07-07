"""Generated from Smithy shape ``com.amazonaws.budgets#CreateNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.notification
    import aws_sdk_budgets.types.subscribers


class CreateNotificationRequest(TypedDict, closed=True):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget that you want to create a notification for.</p>"""
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget that you want Amazon Web Services to notify you about. Budget names must be unique within an account.</p>"""
    notification: "aws_sdk_budgets.types.notification.Notification"
    """<p>The notification that you want to create.</p>"""
    subscribers: "aws_sdk_budgets.types.subscribers.Subscribers"
    """<p>A list of subscribers that you want to associate with the notification. Each notification can have one SNS subscriber and up to 10 email subscribers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNotificationRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import aws_sdk_budgets.types.notification

    out["Notification"] = aws_sdk_budgets.types.notification.serialize_aws_json_1_1(
        value["notification"]
    )
    import aws_sdk_budgets.types.subscribers

    out["Subscribers"] = aws_sdk_budgets.types.subscribers.serialize_aws_json_1_1(
        value["subscribers"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNotificationRequest:
    out: CreateNotificationRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("CreateNotificationRequest.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("CreateNotificationRequest.budget_name required")
    if "Notification" in data:
        import aws_sdk_budgets.types.notification

        out["notification"] = (
            aws_sdk_budgets.types.notification.deserialize_aws_json_1_1(
                data["Notification"]
            )
        )
    else:
        raise DeserializationError("CreateNotificationRequest.notification required")
    if "Subscribers" in data:
        import aws_sdk_budgets.types.subscribers

        out["subscribers"] = aws_sdk_budgets.types.subscribers.deserialize_aws_json_1_1(
            data["Subscribers"]
        )
    else:
        raise DeserializationError("CreateNotificationRequest.subscribers required")
    return out
