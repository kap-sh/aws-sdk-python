"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetHLSStreamingSessionURLOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.hls_streaming_session_url


class GetHLSStreamingSessionURLOutput(TypedDict):
    hls_streaming_session_url: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.hls_streaming_session_url.HLSStreamingSessionURL"
    ]
    """<p>The URL (containing the session token) that a media player can use to retrieve the HLS master playlist.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHLSStreamingSessionURLOutput) -> dict:
    out: dict = {}
    if "hls_streaming_session_url" in value:
        out["HLSStreamingSessionURL"] = value["hls_streaming_session_url"]
    return out


def deserialize_json(data: dict) -> GetHLSStreamingSessionURLOutput:
    out: GetHLSStreamingSessionURLOutput = {}  # type: ignore[typeddict-item]
    if "HLSStreamingSessionURL" in data:
        out["hls_streaming_session_url"] = data["HLSStreamingSessionURL"]
    return out
