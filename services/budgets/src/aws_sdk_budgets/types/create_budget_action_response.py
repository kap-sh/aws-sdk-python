"""Generated from Smithy shape ``com.amazonaws.budgets#CreateBudgetActionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.action_id
    import aws_sdk_budgets.types.budget_name


class CreateBudgetActionResponse(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    action_id: "aws_sdk_budgets.types.action_id.ActionId"
    """<p> A system-generated universally unique identifier (UUID) for the action. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBudgetActionResponse) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    out["ActionId"] = value["action_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBudgetActionResponse:
    out: CreateBudgetActionResponse = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("CreateBudgetActionResponse.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("CreateBudgetActionResponse.budget_name required")
    if "ActionId" in data:
        out["action_id"] = data["ActionId"]
    else:
        raise DeserializationError("CreateBudgetActionResponse.action_id required")
    return out
