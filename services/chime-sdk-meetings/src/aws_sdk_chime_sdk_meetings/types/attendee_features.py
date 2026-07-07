"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#AttendeeFeatures``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.attendee_max


class AttendeeFeatures(TypedDict, closed=True):
    max_count: NotRequired["aws_sdk_chime_sdk_meetings.types.attendee_max.AttendeeMax"]
    """<p>The maximum number of attendees allowed into the meeting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttendeeFeatures) -> dict:
    out: dict = {}
    if "max_count" in value:
        out["MaxCount"] = value["max_count"]
    return out


def deserialize_json(data: dict) -> AttendeeFeatures:
    out: AttendeeFeatures = {}  # type: ignore[typeddict-item]
    if "MaxCount" in data:
        out["max_count"] = data["MaxCount"]
    return out
