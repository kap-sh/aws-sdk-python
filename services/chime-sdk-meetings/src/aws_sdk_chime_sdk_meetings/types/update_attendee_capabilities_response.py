"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#UpdateAttendeeCapabilitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.attendee


class UpdateAttendeeCapabilitiesResponse(TypedDict):
    attendee: NotRequired["aws_sdk_chime_sdk_meetings.types.attendee.Attendee"]
    """<p>The updated attendee data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAttendeeCapabilitiesResponse) -> dict:
    out: dict = {}
    if "attendee" in value:
        import aws_sdk_chime_sdk_meetings.types.attendee

        out["Attendee"] = aws_sdk_chime_sdk_meetings.types.attendee.serialize_json(
            value["attendee"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAttendeeCapabilitiesResponse:
    out: UpdateAttendeeCapabilitiesResponse = {}  # type: ignore[typeddict-item]
    if "Attendee" in data:
        import aws_sdk_chime_sdk_meetings.types.attendee

        out["attendee"] = aws_sdk_chime_sdk_meetings.types.attendee.deserialize_json(
            data["Attendee"]
        )
    return out
