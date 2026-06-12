"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#GetAttendeeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.attendee


class GetAttendeeResponse(TypedDict):
    attendee: NotRequired["aws_sdk_chime_sdk_meetings.types.attendee.Attendee"]
    """<p>The Amazon Chime SDK attendee information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAttendeeResponse) -> dict:
    out: dict = {}
    if "attendee" in value:
        import aws_sdk_chime_sdk_meetings.types.attendee

        out["Attendee"] = aws_sdk_chime_sdk_meetings.types.attendee.serialize_json(
            value["attendee"]
        )
    return out


def deserialize_json(data: dict) -> GetAttendeeResponse:
    out: GetAttendeeResponse = {}  # type: ignore[typeddict-item]
    if "Attendee" in data:
        import aws_sdk_chime_sdk_meetings.types.attendee

        out["attendee"] = aws_sdk_chime_sdk_meetings.types.attendee.deserialize_json(
            data["Attendee"]
        )
    return out
