"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListPrivacyBudgetTemplatesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.privacy_budget_template_summary_list


class ListPrivacyBudgetTemplatesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    privacy_budget_template_summaries: "aws_sdk_cleanrooms.types.privacy_budget_template_summary_list.PrivacyBudgetTemplateSummaryList"
    """<p>An array that summarizes the privacy budget templates. The summary includes collaboration information, creation information, and privacy budget type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivacyBudgetTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.privacy_budget_template_summary_list

    out["privacyBudgetTemplateSummaries"] = (
        aws_sdk_cleanrooms.types.privacy_budget_template_summary_list.serialize_json(
            value["privacy_budget_template_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListPrivacyBudgetTemplatesOutput:
    out: ListPrivacyBudgetTemplatesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "privacyBudgetTemplateSummaries" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template_summary_list

        out["privacy_budget_template_summaries"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_summary_list.deserialize_json(
                data["privacyBudgetTemplateSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListPrivacyBudgetTemplatesOutput.privacy_budget_template_summaries required"
        )
    return out
