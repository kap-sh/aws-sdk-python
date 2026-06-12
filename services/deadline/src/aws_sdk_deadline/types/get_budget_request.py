"""Generated from Smithy shape ``com.amazonaws.deadline#GetBudgetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.budget_id
    import aws_sdk_deadline.types.farm_id


class GetBudgetRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm connected to the budget.</p>"""
    budget_id: "aws_sdk_deadline.types.budget_id.BudgetId"
    """<p>The budget ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBudgetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBudgetRequest:
    out: GetBudgetRequest = {}  # type: ignore[typeddict-item]
    return out
