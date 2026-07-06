"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.action
    import aws_sdk_budgets.types.budget_name


class DescribeBudgetActionResponse(TypedDict, closed=True):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    action: "aws_sdk_budgets.types.action.Action"
    """<p> A budget action resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetActionResponse) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import aws_sdk_budgets.types.action

    out["Action"] = aws_sdk_budgets.types.action.serialize_aws_json_1_1(value["action"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetActionResponse:
    out: DescribeBudgetActionResponse = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("DescribeBudgetActionResponse.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("DescribeBudgetActionResponse.budget_name required")
    if "Action" in data:
        import aws_sdk_budgets.types.action

        out["action"] = aws_sdk_budgets.types.action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("DescribeBudgetActionResponse.action required")
    return out
