"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListAnalysisTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListAnalysisTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    analysis_template_summaries: "aws_sdk_cleanrooms.types.analysis_template_summary_list.AnalysisTemplateSummaryList"
    """<p>Lists analysis template metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalysisTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.analysis_template_summary_list

    out["analysisTemplateSummaries"] = (
        aws_sdk_cleanrooms.types.analysis_template_summary_list.serialize_json(
            value["analysis_template_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAnalysisTemplatesOutput:
    out: ListAnalysisTemplatesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "analysisTemplateSummaries" in data:
        import aws_sdk_cleanrooms.types.analysis_template_summary_list

        out["analysis_template_summaries"] = (
            aws_sdk_cleanrooms.types.analysis_template_summary_list.deserialize_json(
                data["analysisTemplateSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAnalysisTemplatesOutput.analysis_template_summaries required"
        )
    return out
