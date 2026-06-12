"""Generated from Smithy shape ``com.amazonaws.budgets#CreateBudgetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.budget
    import aws_sdk_budgets.types.notification_with_subscribers_list
    import aws_sdk_budgets.types.resource_tag_list


class CreateBudgetRequest(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget.</p>"""
    budget: "aws_sdk_budgets.types.budget.Budget"
    """<p>The budget object that you want to create.</p>"""
    notifications_with_subscribers: NotRequired[
        "aws_sdk_budgets.types.notification_with_subscribers_list.NotificationWithSubscribersList"
    ]
    """<p>A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your <code>CreateBudget</code> call, Amazon Web Services creates the notifications and subscribers for you.</p>"""
    resource_tags: NotRequired[
        "aws_sdk_budgets.types.resource_tag_list.ResourceTagList"
    ]
    """<p>An optional list of tags to associate with the specified budget. Each tag consists of a key and a value, and each key must be unique for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBudgetRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    import aws_sdk_budgets.types.budget

    out["Budget"] = aws_sdk_budgets.types.budget.serialize_aws_json_1_1(value["budget"])
    if "notifications_with_subscribers" in value:
        import aws_sdk_budgets.types.notification_with_subscribers_list

        out["NotificationsWithSubscribers"] = (
            aws_sdk_budgets.types.notification_with_subscribers_list.serialize_aws_json_1_1(
                value["notifications_with_subscribers"]
            )
        )
    if "resource_tags" in value:
        import aws_sdk_budgets.types.resource_tag_list

        out["ResourceTags"] = (
            aws_sdk_budgets.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBudgetRequest:
    out: CreateBudgetRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("CreateBudgetRequest.account_id required")
    if "Budget" in data:
        import aws_sdk_budgets.types.budget

        out["budget"] = aws_sdk_budgets.types.budget.deserialize_aws_json_1_1(
            data["Budget"]
        )
    else:
        raise DeserializationError("CreateBudgetRequest.budget required")
    if "NotificationsWithSubscribers" in data:
        import aws_sdk_budgets.types.notification_with_subscribers_list

        out["notifications_with_subscribers"] = (
            aws_sdk_budgets.types.notification_with_subscribers_list.deserialize_aws_json_1_1(
                data["NotificationsWithSubscribers"]
            )
        )
    if "ResourceTags" in data:
        import aws_sdk_budgets.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_budgets.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    return out
