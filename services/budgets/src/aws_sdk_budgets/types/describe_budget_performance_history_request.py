"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetPerformanceHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.generic_string
    import aws_sdk_budgets.types.max_results
    import aws_sdk_budgets.types.time_period


class DescribeBudgetPerformanceHistoryRequest(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    time_period: NotRequired["aws_sdk_budgets.types.time_period.TimePeriod"]
    """<p>Retrieves how often the budget went into an <code>ALARM</code> state for the specified time period.</p>"""
    max_results: NotRequired["aws_sdk_budgets.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetPerformanceHistoryRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetPerformanceHistoryRequest:
    out: DescribeBudgetPerformanceHistoryRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "DescribeBudgetPerformanceHistoryRequest.account_id required"
        )
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError(
            "DescribeBudgetPerformanceHistoryRequest.budget_name required"
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
