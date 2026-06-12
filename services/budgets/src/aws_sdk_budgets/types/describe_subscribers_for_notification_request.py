"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeSubscribersForNotificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.generic_string
    import aws_sdk_budgets.types.max_results
    import aws_sdk_budgets.types.notification


class DescribeSubscribersForNotificationRequest(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget whose subscribers you want descriptions of.</p>"""
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget whose subscribers you want descriptions of.</p>"""
    notification: "aws_sdk_budgets.types.notification.Notification"
    """<p>The notification whose subscribers you want to list.</p>"""
    max_results: NotRequired["aws_sdk_budgets.types.max_results.MaxResults"]
    """<p>An optional integer that represents how many entries a paginated response contains.</p>"""
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]
    """<p>The pagination token that you include in your request to indicate the next set of results that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscribersForNotificationRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import aws_sdk_budgets.types.notification

    out["Notification"] = aws_sdk_budgets.types.notification.serialize_aws_json_1_1(
        value["notification"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscribersForNotificationRequest:
    out: DescribeSubscribersForNotificationRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "DescribeSubscribersForNotificationRequest.account_id required"
        )
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError(
            "DescribeSubscribersForNotificationRequest.budget_name required"
        )
    if "Notification" in data:
        import aws_sdk_budgets.types.notification

        out["notification"] = (
            aws_sdk_budgets.types.notification.deserialize_aws_json_1_1(
                data["Notification"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeSubscribersForNotificationRequest.notification required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
