"""Generated from Smithy shape ``com.amazonaws.deadline#CreateBudgetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.budget_id


class CreateBudgetResponse(TypedDict):
    budget_id: "aws_sdk_deadline.types.budget_id.BudgetId"
    """<p>The budget ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBudgetResponse) -> dict:
    out: dict = {}
    out["budgetId"] = value["budget_id"]
    return out


def deserialize_json(data: dict) -> CreateBudgetResponse:
    out: CreateBudgetResponse = {}  # type: ignore[typeddict-item]
    if "budgetId" in data:
        out["budget_id"] = data["budgetId"]
    else:
        raise DeserializationError("CreateBudgetResponse.budget_id required")
    return out
