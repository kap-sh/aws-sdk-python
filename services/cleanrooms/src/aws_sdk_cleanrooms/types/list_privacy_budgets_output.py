"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListPrivacyBudgetsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.privacy_budget_summary_list


class ListPrivacyBudgetsOutput(TypedDict):
    privacy_budget_summaries: (
        "aws_sdk_cleanrooms.types.privacy_budget_summary_list.PrivacyBudgetSummaryList"
    )
    """<p>An array that summarizes the privacy budgets. The summary includes collaboration information, membership information, privacy budget template information, and privacy budget details.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivacyBudgetsOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.privacy_budget_summary_list

    out["privacyBudgetSummaries"] = (
        aws_sdk_cleanrooms.types.privacy_budget_summary_list.serialize_json(
            value["privacy_budget_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPrivacyBudgetsOutput:
    out: ListPrivacyBudgetsOutput = {}  # type: ignore[typeddict-item]
    if "privacyBudgetSummaries" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_summary_list

        out["privacy_budget_summaries"] = (
            aws_sdk_cleanrooms.types.privacy_budget_summary_list.deserialize_json(
                data["privacyBudgetSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListPrivacyBudgetsOutput.privacy_budget_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
