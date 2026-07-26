"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#AttendeeIdItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.guid_string


class AttendeeIdItem(TypedDict, closed=True):
    attendee_id: "capo_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>A list of one or more attendee IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttendeeIdItem) -> dict:
    out: dict = {}
    out["AttendeeId"] = value["attendee_id"]
    return out


def deserialize_json(data: dict) -> AttendeeIdItem:
    out: AttendeeIdItem = {}  # type: ignore[typeddict-item]
    if "AttendeeId" in data:
        out["attendee_id"] = data["AttendeeId"]
    else:
        raise DeserializationError("AttendeeIdItem.attendee_id required")
    return out
