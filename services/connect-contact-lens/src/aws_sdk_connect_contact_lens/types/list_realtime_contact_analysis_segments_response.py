"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#ListRealtimeContactAnalysisSegmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.next_token
    import aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segments


class ListRealtimeContactAnalysisSegmentsResponse(TypedDict):
    segments: NotRequired[
        "aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segments.RealtimeContactAnalysisSegments"
    ]
    """<p>An analyzed transcript or category.</p>"""
    next_token: NotRequired["aws_sdk_connect_contact_lens.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results. If response includes <code>nextToken</code> there are two possible scenarios:</p> <ul> <li> <p>There are more segments so another call is required to get them.</p> </li> <li> <p>There are no more segments at this time, but more may be available later (real-time analysis is in progress) so the client should call the operation again to get new segments.</p> </li> </ul> <p>If response does not include <code>nextToken</code>, the analysis is completed (successfully or failed) and there are no more segments to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRealtimeContactAnalysisSegmentsResponse) -> dict:
    out: dict = {}
    if "segments" in value:
        import aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segments

        out["Segments"] = (
            aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segments.serialize_json(
                value["segments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRealtimeContactAnalysisSegmentsResponse:
    out: ListRealtimeContactAnalysisSegmentsResponse = {}  # type: ignore[typeddict-item]
    if "Segments" in data:
        import aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segments

        out["segments"] = (
            aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segments.deserialize_json(
                data["Segments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
