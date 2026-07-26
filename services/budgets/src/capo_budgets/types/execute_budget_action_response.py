"""Generated from Smithy shape ``com.amazonaws.budgets#ExecuteBudgetActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.action_id
    import capo_budgets.types.budget_name
    import capo_budgets.types.execution_type


class ExecuteBudgetActionResponse(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    action_id: "capo_budgets.types.action_id.ActionId"
    """<p> A system-generated universally unique identifier (UUID) for the action. </p>"""
    execution_type: "capo_budgets.types.execution_type.ExecutionType"
    """<p> The type of execution. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteBudgetActionResponse) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    out["ActionId"] = value["action_id"]
    import capo_budgets.types.execution_type

    out["ExecutionType"] = capo_budgets.types.execution_type.serialize_aws_json_1_1(
        value["execution_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteBudgetActionResponse:
    out: ExecuteBudgetActionResponse = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("ExecuteBudgetActionResponse.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("ExecuteBudgetActionResponse.budget_name required")
    if "ActionId" in data:
        out["action_id"] = data["ActionId"]
    else:
        raise DeserializationError("ExecuteBudgetActionResponse.action_id required")
    if "ExecutionType" in data:
        import capo_budgets.types.execution_type

        out["execution_type"] = (
            capo_budgets.types.execution_type.deserialize_aws_json_1_1(
                data["ExecutionType"]
            )
        )
    else:
        raise DeserializationError(
            "ExecuteBudgetActionResponse.execution_type required"
        )
    return out
