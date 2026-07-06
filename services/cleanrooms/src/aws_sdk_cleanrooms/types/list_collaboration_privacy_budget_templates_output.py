"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationPrivacyBudgetTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_privacy_budget_template_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListCollaborationPrivacyBudgetTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    collaboration_privacy_budget_template_summaries: "aws_sdk_cleanrooms.types.collaboration_privacy_budget_template_summary_list.CollaborationPrivacyBudgetTemplateSummaryList"
    """<p>An array that summarizes the collaboration privacy budget templates. The summary includes collaboration information, creation information, the privacy budget type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationPrivacyBudgetTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.collaboration_privacy_budget_template_summary_list

    out["collaborationPrivacyBudgetTemplateSummaries"] = (
        aws_sdk_cleanrooms.types.collaboration_privacy_budget_template_summary_list.serialize_json(
            value["collaboration_privacy_budget_template_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationPrivacyBudgetTemplatesOutput:
    out: ListCollaborationPrivacyBudgetTemplatesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "collaborationPrivacyBudgetTemplateSummaries" in data:
        import aws_sdk_cleanrooms.types.collaboration_privacy_budget_template_summary_list

        out["collaboration_privacy_budget_template_summaries"] = (
            aws_sdk_cleanrooms.types.collaboration_privacy_budget_template_summary_list.deserialize_json(
                data["collaborationPrivacyBudgetTemplateSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationPrivacyBudgetTemplatesOutput.collaboration_privacy_budget_template_summaries required"
        )
    return out
