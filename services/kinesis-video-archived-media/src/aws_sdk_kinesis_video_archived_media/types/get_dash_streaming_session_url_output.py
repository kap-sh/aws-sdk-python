"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetDASHStreamingSessionURLOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.dash_streaming_session_url


class GetDASHStreamingSessionURLOutput(TypedDict):
    dash_streaming_session_url: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.dash_streaming_session_url.DASHStreamingSessionURL"
    ]
    """<p>The URL (containing the session token) that a media player can use to retrieve the MPEG-DASH manifest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDASHStreamingSessionURLOutput) -> dict:
    out: dict = {}
    if "dash_streaming_session_url" in value:
        out["DASHStreamingSessionURL"] = value["dash_streaming_session_url"]
    return out


def deserialize_json(data: dict) -> GetDASHStreamingSessionURLOutput:
    out: GetDASHStreamingSessionURLOutput = {}  # type: ignore[typeddict-item]
    if "DASHStreamingSessionURL" in data:
        out["dash_streaming_session_url"] = data["DASHStreamingSessionURL"]
    return out
