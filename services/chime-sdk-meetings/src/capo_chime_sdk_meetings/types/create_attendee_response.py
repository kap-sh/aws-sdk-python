"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateAttendeeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee


class CreateAttendeeResponse(TypedDict, closed=True):
    attendee: NotRequired["capo_chime_sdk_meetings.types.attendee.Attendee"]
    """<p>The attendee information, including attendee ID and join token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAttendeeResponse) -> dict:
    out: dict = {}
    if "attendee" in value:
        import capo_chime_sdk_meetings.types.attendee

        out["Attendee"] = capo_chime_sdk_meetings.types.attendee.serialize_json(
            value["attendee"]
        )
    return out


def deserialize_json(data: dict) -> CreateAttendeeResponse:
    out: CreateAttendeeResponse = {}  # type: ignore[typeddict-item]
    if "Attendee" in data:
        import capo_chime_sdk_meetings.types.attendee

        out["attendee"] = capo_chime_sdk_meetings.types.attendee.deserialize_json(
            data["Attendee"]
        )
    return out
