"""Generated from Smithy shape ``com.amazonaws.connectparticipant#WebRTCConnection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.attendee
    import aws_sdk_connectparticipant.types.web_rtc_meeting


class WebRTCConnection(TypedDict):
    attendee: NotRequired["aws_sdk_connectparticipant.types.attendee.Attendee"]
    meeting: NotRequired[
        "aws_sdk_connectparticipant.types.web_rtc_meeting.WebRTCMeeting"
    ]
    """<p>A meeting created using the Amazon Chime SDK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebRTCConnection) -> dict:
    out: dict = {}
    if "attendee" in value:
        import aws_sdk_connectparticipant.types.attendee

        out["Attendee"] = aws_sdk_connectparticipant.types.attendee.serialize_json(
            value["attendee"]
        )
    if "meeting" in value:
        import aws_sdk_connectparticipant.types.web_rtc_meeting

        out["Meeting"] = (
            aws_sdk_connectparticipant.types.web_rtc_meeting.serialize_json(
                value["meeting"]
            )
        )
    return out


def deserialize_json(data: dict) -> WebRTCConnection:
    out: WebRTCConnection = {}  # type: ignore[typeddict-item]
    if "Attendee" in data:
        import aws_sdk_connectparticipant.types.attendee

        out["attendee"] = aws_sdk_connectparticipant.types.attendee.deserialize_json(
            data["Attendee"]
        )
    if "Meeting" in data:
        import aws_sdk_connectparticipant.types.web_rtc_meeting

        out["meeting"] = (
            aws_sdk_connectparticipant.types.web_rtc_meeting.deserialize_json(
                data["Meeting"]
            )
        )
    return out
