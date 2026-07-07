"""Generated from Smithy shape ``com.amazonaws.budgets#CreateSubscriberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.notification
    import aws_sdk_budgets.types.subscriber


class CreateSubscriberRequest(TypedDict, closed=True):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget that you want to create a subscriber for.</p>"""
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget that you want to subscribe to. Budget names must be unique within an account.</p>"""
    notification: "aws_sdk_budgets.types.notification.Notification"
    """<p>The notification that you want to create a subscriber for.</p>"""
    subscriber: "aws_sdk_budgets.types.subscriber.Subscriber"
    """<p>The subscriber that you want to associate with a budget notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSubscriberRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import aws_sdk_budgets.types.notification

    out["Notification"] = aws_sdk_budgets.types.notification.serialize_aws_json_1_1(
        value["notification"]
    )
    import aws_sdk_budgets.types.subscriber

    out["Subscriber"] = aws_sdk_budgets.types.subscriber.serialize_aws_json_1_1(
        value["subscriber"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSubscriberRequest:
    out: CreateSubscriberRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("CreateSubscriberRequest.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("CreateSubscriberRequest.budget_name required")
    if "Notification" in data:
        import aws_sdk_budgets.types.notification

        out["notification"] = (
            aws_sdk_budgets.types.notification.deserialize_aws_json_1_1(
                data["Notification"]
            )
        )
    else:
        raise DeserializationError("CreateSubscriberRequest.notification required")
    if "Subscriber" in data:
        import aws_sdk_budgets.types.subscriber

        out["subscriber"] = aws_sdk_budgets.types.subscriber.deserialize_aws_json_1_1(
            data["Subscriber"]
        )
    else:
        raise DeserializationError("CreateSubscriberRequest.subscriber required")
    return out
