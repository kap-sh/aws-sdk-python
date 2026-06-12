"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetActionHistoriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.action_histories
    import aws_sdk_budgets.types.generic_string


class DescribeBudgetActionHistoriesResponse(TypedDict):
    action_histories: "aws_sdk_budgets.types.action_histories.ActionHistories"
    """<p> The historical record of the budget action resource. </p>"""
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetActionHistoriesResponse) -> dict:
    out: dict = {}
    import aws_sdk_budgets.types.action_histories

    out["ActionHistories"] = (
        aws_sdk_budgets.types.action_histories.serialize_aws_json_1_1(
            value["action_histories"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetActionHistoriesResponse:
    out: DescribeBudgetActionHistoriesResponse = {}  # type: ignore[typeddict-item]
    if "ActionHistories" in data:
        import aws_sdk_budgets.types.action_histories

        out["action_histories"] = (
            aws_sdk_budgets.types.action_histories.deserialize_aws_json_1_1(
                data["ActionHistories"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeBudgetActionHistoriesResponse.action_histories required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
