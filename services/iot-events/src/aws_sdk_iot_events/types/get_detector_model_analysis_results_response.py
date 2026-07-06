"""Generated from Smithy shape ``com.amazonaws.iotevents#GetDetectorModelAnalysisResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.analysis_results
    import aws_sdk_iot_events.types.next_token


class GetDetectorModelAnalysisResultsResponse(TypedDict, closed=True):
    analysis_results: NotRequired[
        "aws_sdk_iot_events.types.analysis_results.AnalysisResults"
    ]
    """<p>Contains information about one or more analysis results.</p>"""
    next_token: NotRequired["aws_sdk_iot_events.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results, or <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDetectorModelAnalysisResultsResponse) -> dict:
    out: dict = {}
    if "analysis_results" in value:
        import aws_sdk_iot_events.types.analysis_results

        out["analysisResults"] = (
            aws_sdk_iot_events.types.analysis_results.serialize_json(
                value["analysis_results"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDetectorModelAnalysisResultsResponse:
    out: GetDetectorModelAnalysisResultsResponse = {}  # type: ignore[typeddict-item]
    if "analysisResults" in data:
        import aws_sdk_iot_events.types.analysis_results

        out["analysis_results"] = (
            aws_sdk_iot_events.types.analysis_results.deserialize_json(
                data["analysisResults"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
