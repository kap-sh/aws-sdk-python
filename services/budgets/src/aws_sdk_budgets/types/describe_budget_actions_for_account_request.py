"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetActionsForAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.generic_string
    import aws_sdk_budgets.types.max_results


class DescribeBudgetActionsForAccountRequest(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    max_results: NotRequired["aws_sdk_budgets.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetActionsForAccountRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetActionsForAccountRequest:
    out: DescribeBudgetActionsForAccountRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "DescribeBudgetActionsForAccountRequest.account_id required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
