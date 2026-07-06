"""Generated from Smithy shape ``com.amazonaws.budgets#UpdateSubscriberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.notification
    import aws_sdk_budgets.types.subscriber


class UpdateSubscriberRequest(TypedDict, closed=True):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget whose subscriber you want to update.</p>"""
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget whose subscriber you want to update.</p>"""
    notification: "aws_sdk_budgets.types.notification.Notification"
    """<p>The notification whose subscriber you want to update.</p>"""
    old_subscriber: "aws_sdk_budgets.types.subscriber.Subscriber"
    """<p>The previous subscriber that is associated with a budget notification.</p>"""
    new_subscriber: "aws_sdk_budgets.types.subscriber.Subscriber"
    """<p>The updated subscriber that is associated with a budget notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubscriberRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import aws_sdk_budgets.types.notification

    out["Notification"] = aws_sdk_budgets.types.notification.serialize_aws_json_1_1(
        value["notification"]
    )
    import aws_sdk_budgets.types.subscriber

    out["OldSubscriber"] = aws_sdk_budgets.types.subscriber.serialize_aws_json_1_1(
        value["old_subscriber"]
    )
    import aws_sdk_budgets.types.subscriber

    out["NewSubscriber"] = aws_sdk_budgets.types.subscriber.serialize_aws_json_1_1(
        value["new_subscriber"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubscriberRequest:
    out: UpdateSubscriberRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("UpdateSubscriberRequest.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("UpdateSubscriberRequest.budget_name required")
    if "Notification" in data:
        import aws_sdk_budgets.types.notification

        out["notification"] = (
            aws_sdk_budgets.types.notification.deserialize_aws_json_1_1(
                data["Notification"]
            )
        )
    else:
        raise DeserializationError("UpdateSubscriberRequest.notification required")
    if "OldSubscriber" in data:
        import aws_sdk_budgets.types.subscriber

        out["old_subscriber"] = (
            aws_sdk_budgets.types.subscriber.deserialize_aws_json_1_1(
                data["OldSubscriber"]
            )
        )
    else:
        raise DeserializationError("UpdateSubscriberRequest.old_subscriber required")
    if "NewSubscriber" in data:
        import aws_sdk_budgets.types.subscriber

        out["new_subscriber"] = (
            aws_sdk_budgets.types.subscriber.deserialize_aws_json_1_1(
                data["NewSubscriber"]
            )
        )
    else:
        raise DeserializationError("UpdateSubscriberRequest.new_subscriber required")
    return out
