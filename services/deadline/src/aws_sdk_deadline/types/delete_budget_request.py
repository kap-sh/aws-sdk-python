"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteBudgetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.budget_id
    import aws_sdk_deadline.types.farm_id


class DeleteBudgetRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to remove from the budget.</p>"""
    budget_id: "aws_sdk_deadline.types.budget_id.BudgetId"
    """<p>The budget ID of the budget to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBudgetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBudgetRequest:
    out: DeleteBudgetRequest = {}  # type: ignore[typeddict-item]
    return out
