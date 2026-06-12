"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.nullable_boolean


class DescribeBudgetRequest(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget that you want a description of.</p>"""
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget that you want a description of.</p>"""
    show_filter_expression: NotRequired[
        "aws_sdk_budgets.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether the response includes the filter expression associated with the budget. By showing the filter expression, you can see detailed filtering logic applied to the budget, such as Amazon Web Services services or tags that are being tracked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    if "show_filter_expression" in value:
        out["ShowFilterExpression"] = value["show_filter_expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetRequest:
    out: DescribeBudgetRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("DescribeBudgetRequest.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("DescribeBudgetRequest.budget_name required")
    if "ShowFilterExpression" in data:
        out["show_filter_expression"] = data["ShowFilterExpression"]
    return out
