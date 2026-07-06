"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetPerformanceHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_budgets.types.budget_performance_history
    import aws_sdk_budgets.types.generic_string


class DescribeBudgetPerformanceHistoryResponse(TypedDict, closed=True):
    budget_performance_history: NotRequired[
        "aws_sdk_budgets.types.budget_performance_history.BudgetPerformanceHistory"
    ]
    """<p>The history of how often the budget has gone into an <code>ALARM</code> state.</p> <p>For <code>DAILY</code> budgets, the history saves the state of the budget for the last 60 days. For <code>MONTHLY</code> budgets, the history saves the state of the budget for the current month plus the last 12 months. For <code>QUARTERLY</code> budgets, the history saves the state of the budget for the last four quarters.</p>"""
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetPerformanceHistoryResponse) -> dict:
    out: dict = {}
    if "budget_performance_history" in value:
        import aws_sdk_budgets.types.budget_performance_history

        out["BudgetPerformanceHistory"] = (
            aws_sdk_budgets.types.budget_performance_history.serialize_aws_json_1_1(
                value["budget_performance_history"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetPerformanceHistoryResponse:
    out: DescribeBudgetPerformanceHistoryResponse = {}  # type: ignore[typeddict-item]
    if "BudgetPerformanceHistory" in data:
        import aws_sdk_budgets.types.budget_performance_history

        out["budget_performance_history"] = (
            aws_sdk_budgets.types.budget_performance_history.deserialize_aws_json_1_1(
                data["BudgetPerformanceHistory"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
