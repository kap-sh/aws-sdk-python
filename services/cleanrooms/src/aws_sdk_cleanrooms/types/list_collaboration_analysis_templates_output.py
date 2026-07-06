"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationAnalysisTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_analysis_template_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListCollaborationAnalysisTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    collaboration_analysis_template_summaries: "aws_sdk_cleanrooms.types.collaboration_analysis_template_summary_list.CollaborationAnalysisTemplateSummaryList"
    """<p>The metadata of the analysis template within a collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationAnalysisTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.collaboration_analysis_template_summary_list

    out["collaborationAnalysisTemplateSummaries"] = (
        aws_sdk_cleanrooms.types.collaboration_analysis_template_summary_list.serialize_json(
            value["collaboration_analysis_template_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationAnalysisTemplatesOutput:
    out: ListCollaborationAnalysisTemplatesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "collaborationAnalysisTemplateSummaries" in data:
        import aws_sdk_cleanrooms.types.collaboration_analysis_template_summary_list

        out["collaboration_analysis_template_summaries"] = (
            aws_sdk_cleanrooms.types.collaboration_analysis_template_summary_list.deserialize_json(
                data["collaborationAnalysisTemplateSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationAnalysisTemplatesOutput.collaboration_analysis_template_summaries required"
        )
    return out
