"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#MeetingFeaturesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee_features
    import capo_chime_sdk_meetings.types.audio_features
    import capo_chime_sdk_meetings.types.content_features
    import capo_chime_sdk_meetings.types.video_features


class MeetingFeaturesConfiguration(TypedDict, closed=True):
    audio: NotRequired["capo_chime_sdk_meetings.types.audio_features.AudioFeatures"]
    """<p>The configuration settings for the audio features available to a meeting.</p>"""
    video: NotRequired["capo_chime_sdk_meetings.types.video_features.VideoFeatures"]
    """<p>The configuration settings for the video features available to a meeting.</p>"""
    content: NotRequired[
        "capo_chime_sdk_meetings.types.content_features.ContentFeatures"
    ]
    """<p>The configuration settings for the content features available to a meeting.</p>"""
    attendee: NotRequired[
        "capo_chime_sdk_meetings.types.attendee_features.AttendeeFeatures"
    ]
    """<p>The configuration settings for the attendee features available to a meeting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeetingFeaturesConfiguration) -> dict:
    out: dict = {}
    if "audio" in value:
        import capo_chime_sdk_meetings.types.audio_features

        out["Audio"] = capo_chime_sdk_meetings.types.audio_features.serialize_json(
            value["audio"]
        )
    if "video" in value:
        import capo_chime_sdk_meetings.types.video_features

        out["Video"] = capo_chime_sdk_meetings.types.video_features.serialize_json(
            value["video"]
        )
    if "content" in value:
        import capo_chime_sdk_meetings.types.content_features

        out["Content"] = capo_chime_sdk_meetings.types.content_features.serialize_json(
            value["content"]
        )
    if "attendee" in value:
        import capo_chime_sdk_meetings.types.attendee_features

        out["Attendee"] = (
            capo_chime_sdk_meetings.types.attendee_features.serialize_json(
                value["attendee"]
            )
        )
    return out


def deserialize_json(data: dict) -> MeetingFeaturesConfiguration:
    out: MeetingFeaturesConfiguration = {}  # type: ignore[typeddict-item]
    if "Audio" in data:
        import capo_chime_sdk_meetings.types.audio_features

        out["audio"] = capo_chime_sdk_meetings.types.audio_features.deserialize_json(
            data["Audio"]
        )
    if "Video" in data:
        import capo_chime_sdk_meetings.types.video_features

        out["video"] = capo_chime_sdk_meetings.types.video_features.deserialize_json(
            data["Video"]
        )
    if "Content" in data:
        import capo_chime_sdk_meetings.types.content_features

        out["content"] = (
            capo_chime_sdk_meetings.types.content_features.deserialize_json(
                data["Content"]
            )
        )
    if "Attendee" in data:
        import capo_chime_sdk_meetings.types.attendee_features

        out["attendee"] = (
            capo_chime_sdk_meetings.types.attendee_features.deserialize_json(
                data["Attendee"]
            )
        )
    return out
