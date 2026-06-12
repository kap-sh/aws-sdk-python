"""Generated from Smithy shape ``com.amazonaws.budgets#UpdateBudgetActionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.action
    import aws_sdk_budgets.types.budget_name


class UpdateBudgetActionResponse(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    old_action: "aws_sdk_budgets.types.action.Action"
    """<p> The previous action resource information. </p>"""
    new_action: "aws_sdk_budgets.types.action.Action"
    """<p> The updated action resource information. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBudgetActionResponse) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import aws_sdk_budgets.types.action

    out["OldAction"] = aws_sdk_budgets.types.action.serialize_aws_json_1_1(
        value["old_action"]
    )
    import aws_sdk_budgets.types.action

    out["NewAction"] = aws_sdk_budgets.types.action.serialize_aws_json_1_1(
        value["new_action"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBudgetActionResponse:
    out: UpdateBudgetActionResponse = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("UpdateBudgetActionResponse.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("UpdateBudgetActionResponse.budget_name required")
    if "OldAction" in data:
        import aws_sdk_budgets.types.action

        out["old_action"] = aws_sdk_budgets.types.action.deserialize_aws_json_1_1(
            data["OldAction"]
        )
    else:
        raise DeserializationError("UpdateBudgetActionResponse.old_action required")
    if "NewAction" in data:
        import aws_sdk_budgets.types.action

        out["new_action"] = aws_sdk_budgets.types.action.deserialize_aws_json_1_1(
            data["NewAction"]
        )
    else:
        raise DeserializationError("UpdateBudgetActionResponse.new_action required")
    return out
