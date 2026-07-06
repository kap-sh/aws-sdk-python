"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_budgets.types.budget


class DescribeBudgetResponse(TypedDict, closed=True):
    budget: NotRequired["aws_sdk_budgets.types.budget.Budget"]
    """<p>The description of the budget.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetResponse) -> dict:
    out: dict = {}
    if "budget" in value:
        import aws_sdk_budgets.types.budget

        out["Budget"] = aws_sdk_budgets.types.budget.serialize_aws_json_1_1(
            value["budget"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetResponse:
    out: DescribeBudgetResponse = {}  # type: ignore[typeddict-item]
    if "Budget" in data:
        import aws_sdk_budgets.types.budget

        out["budget"] = aws_sdk_budgets.types.budget.deserialize_aws_json_1_1(
            data["Budget"]
        )
    return out
