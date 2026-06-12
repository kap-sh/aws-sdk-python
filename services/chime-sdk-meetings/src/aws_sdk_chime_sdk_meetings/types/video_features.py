"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#VideoFeatures``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.video_resolution


class VideoFeatures(TypedDict):
    max_resolution: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.video_resolution.VideoResolution"
    ]
    """<p>The maximum video resolution for the meeting. Applies to all attendees.</p> <note> <p>Defaults to <code>HD</code>. To use <code>FHD</code>, you must also provide a <code>MeetingFeatures:Attendee:MaxCount</code> value and override the default size limit of 250 attendees.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoFeatures) -> dict:
    out: dict = {}
    if "max_resolution" in value:
        import aws_sdk_chime_sdk_meetings.types.video_resolution

        out["MaxResolution"] = (
            aws_sdk_chime_sdk_meetings.types.video_resolution.serialize_json(
                value["max_resolution"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoFeatures:
    out: VideoFeatures = {}  # type: ignore[typeddict-item]
    if "MaxResolution" in data:
        import aws_sdk_chime_sdk_meetings.types.video_resolution

        out["max_resolution"] = (
            aws_sdk_chime_sdk_meetings.types.video_resolution.deserialize_json(
                data["MaxResolution"]
            )
        )
    return out
