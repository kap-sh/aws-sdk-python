"""Generated from Smithy shape ``com.amazonaws.connect#ConnectionData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.attendee
    import aws_sdk_connect.types.meeting


class ConnectionData(TypedDict):
    attendee: NotRequired["aws_sdk_connect.types.attendee.Attendee"]
    """<p>The attendee information, including attendee ID and join token.</p>"""
    meeting: NotRequired["aws_sdk_connect.types.meeting.Meeting"]
    """<p>A meeting created using the Amazon Chime SDK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionData) -> dict:
    out: dict = {}
    if "attendee" in value:
        import aws_sdk_connect.types.attendee

        out["Attendee"] = aws_sdk_connect.types.attendee.serialize_json(
            value["attendee"]
        )
    if "meeting" in value:
        import aws_sdk_connect.types.meeting

        out["Meeting"] = aws_sdk_connect.types.meeting.serialize_json(value["meeting"])
    return out


def deserialize_json(data: dict) -> ConnectionData:
    out: ConnectionData = {}  # type: ignore[typeddict-item]
    if "Attendee" in data:
        import aws_sdk_connect.types.attendee

        out["attendee"] = aws_sdk_connect.types.attendee.deserialize_json(
            data["Attendee"]
        )
    if "Meeting" in data:
        import aws_sdk_connect.types.meeting

        out["meeting"] = aws_sdk_connect.types.meeting.deserialize_json(data["Meeting"])
    return out
