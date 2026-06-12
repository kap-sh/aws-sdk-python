"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetActionHistoriesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.action_id
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.generic_string
    import aws_sdk_budgets.types.max_results
    import aws_sdk_budgets.types.time_period


class DescribeBudgetActionHistoriesRequest(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    action_id: "aws_sdk_budgets.types.action_id.ActionId"
    """<p> A system-generated universally unique identifier (UUID) for the action. </p>"""
    time_period: NotRequired["aws_sdk_budgets.types.time_period.TimePeriod"]
    max_results: NotRequired["aws_sdk_budgets.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetActionHistoriesRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    out["ActionId"] = value["action_id"]
    if "time_period" in value:
        import aws_sdk_budgets.types.time_period

        out["TimePeriod"] = aws_sdk_budgets.types.time_period.serialize_aws_json_1_1(
            value["time_period"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetActionHistoriesRequest:
    out: DescribeBudgetActionHistoriesRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "DescribeBudgetActionHistoriesRequest.account_id required"
        )
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError(
            "DescribeBudgetActionHistoriesRequest.budget_name required"
        )
    if "ActionId" in data:
        out["action_id"] = data["ActionId"]
    else:
        raise DeserializationError(
            "DescribeBudgetActionHistoriesRequest.action_id required"
        )
    if "TimePeriod" in data:
        import aws_sdk_budgets.types.time_period

        out["time_period"] = aws_sdk_budgets.types.time_period.deserialize_aws_json_1_1(
            data["TimePeriod"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
