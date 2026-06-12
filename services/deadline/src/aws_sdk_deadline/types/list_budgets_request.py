"""Generated from Smithy shape ``com.amazonaws.deadline#ListBudgetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.budget_status
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token


class ListBudgetsRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID associated with the budgets.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    status: NotRequired["aws_sdk_deadline.types.budget_status.BudgetStatus"]
    """<p>The status to list for the budgets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBudgetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBudgetsRequest:
    out: ListBudgetsRequest = {}  # type: ignore[typeddict-item]
    return out
