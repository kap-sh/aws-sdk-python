"""Generated from Smithy shape ``com.amazonaws.connectparticipant#WebRTCMeeting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.guid_string
    import aws_sdk_connectparticipant.types.meeting_features_configuration
    import aws_sdk_connectparticipant.types.web_rtc_media_placement


class WebRTCMeeting(TypedDict, closed=True):
    media_placement: NotRequired[
        "aws_sdk_connectparticipant.types.web_rtc_media_placement.WebRTCMediaPlacement"
    ]
    """<p>The media placement for the meeting.</p>"""
    meeting_features: NotRequired[
        "aws_sdk_connectparticipant.types.meeting_features_configuration.MeetingFeaturesConfiguration"
    ]
    meeting_id: NotRequired["aws_sdk_connectparticipant.types.guid_string.GuidString"]
    """<p>The Amazon Chime SDK meeting ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebRTCMeeting) -> dict:
    out: dict = {}
    if "media_placement" in value:
        import aws_sdk_connectparticipant.types.web_rtc_media_placement

        out["MediaPlacement"] = (
            aws_sdk_connectparticipant.types.web_rtc_media_placement.serialize_json(
                value["media_placement"]
            )
        )
    if "meeting_features" in value:
        import aws_sdk_connectparticipant.types.meeting_features_configuration

        out["MeetingFeatures"] = (
            aws_sdk_connectparticipant.types.meeting_features_configuration.serialize_json(
                value["meeting_features"]
            )
        )
    if "meeting_id" in value:
        out["MeetingId"] = value["meeting_id"]
    return out


def deserialize_json(data: dict) -> WebRTCMeeting:
    out: WebRTCMeeting = {}  # type: ignore[typeddict-item]
    if "MediaPlacement" in data:
        import aws_sdk_connectparticipant.types.web_rtc_media_placement

        out["media_placement"] = (
            aws_sdk_connectparticipant.types.web_rtc_media_placement.deserialize_json(
                data["MediaPlacement"]
            )
        )
    if "MeetingFeatures" in data:
        import aws_sdk_connectparticipant.types.meeting_features_configuration

        out["meeting_features"] = (
            aws_sdk_connectparticipant.types.meeting_features_configuration.deserialize_json(
                data["MeetingFeatures"]
            )
        )
    if "MeetingId" in data:
        out["meeting_id"] = data["MeetingId"]
    return out
