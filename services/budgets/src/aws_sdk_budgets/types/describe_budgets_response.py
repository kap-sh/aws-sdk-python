"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_budgets.types.budgets
    import aws_sdk_budgets.types.generic_string


class DescribeBudgetsResponse(TypedDict):
    budgets: NotRequired["aws_sdk_budgets.types.budgets.Budgets"]
    """<p>A list of budgets.</p>"""
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]
    """<p>The pagination token in the service response that indicates the next set of results that you can retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetsResponse) -> dict:
    out: dict = {}
    if "budgets" in value:
        import aws_sdk_budgets.types.budgets

        out["Budgets"] = aws_sdk_budgets.types.budgets.serialize_aws_json_1_1(
            value["budgets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetsResponse:
    out: DescribeBudgetsResponse = {}  # type: ignore[typeddict-item]
    if "Budgets" in data:
        import aws_sdk_budgets.types.budgets

        out["budgets"] = aws_sdk_budgets.types.budgets.deserialize_aws_json_1_1(
            data["Budgets"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
