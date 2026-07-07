"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeNotificationsForBudgetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.generic_string
    import aws_sdk_budgets.types.max_results


class DescribeNotificationsForBudgetRequest(TypedDict, closed=True):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget whose notifications you want descriptions of.</p>"""
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget whose notifications you want descriptions of.</p>"""
    max_results: NotRequired["aws_sdk_budgets.types.max_results.MaxResults"]
    """<p>An optional integer that represents how many entries a paginated response contains.</p>"""
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]
    """<p>The pagination token that you include in your request to indicate the next set of results that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNotificationsForBudgetRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNotificationsForBudgetRequest:
    out: DescribeNotificationsForBudgetRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "DescribeNotificationsForBudgetRequest.account_id required"
        )
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError(
            "DescribeNotificationsForBudgetRequest.budget_name required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
