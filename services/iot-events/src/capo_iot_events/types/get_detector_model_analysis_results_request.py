"""Generated from Smithy shape ``com.amazonaws.iotevents#GetDetectorModelAnalysisResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.analysis_id
    import capo_iot_events.types.max_analysis_results
    import capo_iot_events.types.next_token


class GetDetectorModelAnalysisResultsRequest(TypedDict, closed=True):
    analysis_id: "capo_iot_events.types.analysis_id.AnalysisId"
    """<p>The ID of the analysis result that you want to retrieve.</p>"""
    next_token: NotRequired["capo_iot_events.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results.</p>"""
    max_results: NotRequired[
        "capo_iot_events.types.max_analysis_results.MaxAnalysisResults"
    ]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDetectorModelAnalysisResultsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDetectorModelAnalysisResultsRequest:
    out: GetDetectorModelAnalysisResultsRequest = {}  # type: ignore[typeddict-item]
    return out
