"""Generated from Smithy shape ``com.amazonaws.connect#ListRealtimeContactAnalysisSegmentsV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.large_next_token
    import aws_sdk_connect.types.real_time_contact_analysis_status
    import aws_sdk_connect.types.real_time_contact_analysis_supported_channel
    import aws_sdk_connect.types.realtime_contact_analysis_segments


class ListRealtimeContactAnalysisSegmentsV2Response(TypedDict):
    channel: "aws_sdk_connect.types.real_time_contact_analysis_supported_channel.RealTimeContactAnalysisSupportedChannel"
    """<p>The channel of the contact. </p> <important> <p>Only <code>CHAT</code> is supported. This API does not support <code>VOICE</code>. If you attempt to use it for the VOICE channel, an <code>InvalidRequestException</code> error occurs.</p> </important>"""
    status: "aws_sdk_connect.types.real_time_contact_analysis_status.RealTimeContactAnalysisStatus"
    """<p>Status of real-time contact analysis.</p>"""
    segments: "aws_sdk_connect.types.realtime_contact_analysis_segments.RealtimeContactAnalysisSegments"
    """<p>An analyzed transcript or category.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.large_next_token.LargeNextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRealtimeContactAnalysisSegmentsV2Response) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.real_time_contact_analysis_supported_channel

    out["Channel"] = (
        aws_sdk_connect.types.real_time_contact_analysis_supported_channel.serialize_json(
            value["channel"]
        )
    )
    import aws_sdk_connect.types.real_time_contact_analysis_status

    out["Status"] = (
        aws_sdk_connect.types.real_time_contact_analysis_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_connect.types.realtime_contact_analysis_segments

    out["Segments"] = (
        aws_sdk_connect.types.realtime_contact_analysis_segments.serialize_json(
            value["segments"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRealtimeContactAnalysisSegmentsV2Response:
    out: ListRealtimeContactAnalysisSegmentsV2Response = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_supported_channel

        out["channel"] = (
            aws_sdk_connect.types.real_time_contact_analysis_supported_channel.deserialize_json(
                data["Channel"]
            )
        )
    else:
        raise DeserializationError(
            "ListRealtimeContactAnalysisSegmentsV2Response.channel required"
        )
    if "Status" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_status

        out["status"] = (
            aws_sdk_connect.types.real_time_contact_analysis_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "ListRealtimeContactAnalysisSegmentsV2Response.status required"
        )
    if "Segments" in data:
        import aws_sdk_connect.types.realtime_contact_analysis_segments

        out["segments"] = (
            aws_sdk_connect.types.realtime_contact_analysis_segments.deserialize_json(
                data["Segments"]
            )
        )
    else:
        raise DeserializationError(
            "ListRealtimeContactAnalysisSegmentsV2Response.segments required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
