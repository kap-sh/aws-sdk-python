"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAnalysesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_summary_list
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class SearchAnalysesResponse(TypedDict, closed=True):
    analysis_summary_list: NotRequired[
        "capo_quicksight.types.analysis_summary_list.AnalysisSummaryList"
    ]
    """<p>Metadata describing the analyses that you searched for.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request. </p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAnalysesResponse) -> dict:
    out: dict = {}
    if "analysis_summary_list" in value:
        import capo_quicksight.types.analysis_summary_list

        out["AnalysisSummaryList"] = (
            capo_quicksight.types.analysis_summary_list.serialize_json(
                value["analysis_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchAnalysesResponse:
    out: SearchAnalysesResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisSummaryList" in data:
        import capo_quicksight.types.analysis_summary_list

        out["analysis_summary_list"] = (
            capo_quicksight.types.analysis_summary_list.deserialize_json(
                data["AnalysisSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
