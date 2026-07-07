"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#DeleteAttendeeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.guid_string


class DeleteAttendeeRequest(TypedDict, closed=True):
    meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK meeting ID.</p>"""
    attendee_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK attendee ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttendeeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAttendeeRequest:
    out: DeleteAttendeeRequest = {}  # type: ignore[typeddict-item]
    return out
