"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudget``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cleanrooms.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.access_budget_details_list
    import aws_sdk_cleanrooms.types.budgeted_resource_arn
    import aws_sdk_cleanrooms.types.remaining_budget

class AccessBudget(TypedDict):
    resource_arn: "aws_sdk_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
    """<p>The Amazon Resource Name (ARN) of the access budget resource.</p>"""
    details: "aws_sdk_cleanrooms.types.access_budget_details_list.AccessBudgetDetailsList"
    """<p>Detailed budget information including time bounds, remaining budget, and refresh settings.</p>"""
    aggregate_remaining_budget: "aws_sdk_cleanrooms.types.remaining_budget.RemainingBudget"
    """<p>The total remaining budget across all budget parameters, showing the lower value between the per-period budget and lifetime budget for this access budget. For individual parameter budgets, see <code>remainingBudget</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AccessBudget) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_cleanrooms.types.access_budget_details_list
    out["details"] = aws_sdk_cleanrooms.types.access_budget_details_list.serialize_json(value["details"])
    out["aggregateRemainingBudget"] = value["aggregate_remaining_budget"]
    return out


def deserialize_json(data: dict) -> AccessBudget:
    out: AccessBudget = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("AccessBudget.resource_arn required")
    if "details" in data:
        import aws_sdk_cleanrooms.types.access_budget_details_list
        out["details"] = aws_sdk_cleanrooms.types.access_budget_details_list.deserialize_json(data["details"])
    else:
        raise DeserializationError("AccessBudget.details required")
    if "aggregateRemainingBudget" in data:
        out["aggregate_remaining_budget"] = data["aggregateRemainingBudget"]
    else:
        raise DeserializationError("AccessBudget.aggregate_remaining_budget required")
    return out