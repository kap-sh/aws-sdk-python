"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AccessBudget``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cleanroomsml.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.access_budget_details_list
    import aws_sdk_cleanroomsml.types.budget
    import aws_sdk_cleanroomsml.types.budgeted_resource_arn

class AccessBudget(TypedDict):
    resource_arn: "aws_sdk_cleanroomsml.types.budgeted_resource_arn.BudgetedResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that this access budget applies to.</p>"""
    details: "aws_sdk_cleanroomsml.types.access_budget_details_list.AccessBudgetDetailsList"
    """<p>A list of budget details for this resource. Contains active budget periods that apply to the resource.</p>"""
    aggregate_remaining_budget: "aws_sdk_cleanroomsml.types.budget.Budget"
    """<p>The total remaining budget across all active budget periods for this resource.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AccessBudget) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_cleanroomsml.types.access_budget_details_list
    out["details"] = aws_sdk_cleanroomsml.types.access_budget_details_list.serialize_json(value["details"])
    out["aggregateRemainingBudget"] = value["aggregate_remaining_budget"]
    return out


def deserialize_json(data: dict) -> AccessBudget:
    out: AccessBudget = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("AccessBudget.resource_arn required")
    if "details" in data:
        import aws_sdk_cleanroomsml.types.access_budget_details_list
        out["details"] = aws_sdk_cleanroomsml.types.access_budget_details_list.deserialize_json(data["details"])
    else:
        raise DeserializationError("AccessBudget.details required")
    if "aggregateRemainingBudget" in data:
        out["aggregate_remaining_budget"] = data["aggregateRemainingBudget"]
    else:
        raise DeserializationError("AccessBudget.aggregate_remaining_budget required")
    return out