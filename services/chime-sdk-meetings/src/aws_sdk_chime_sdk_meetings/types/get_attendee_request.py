"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#GetAttendeeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.guid_string


class GetAttendeeRequest(TypedDict):
    meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK meeting ID.</p>"""
    attendee_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK attendee ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAttendeeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAttendeeRequest:
    out: GetAttendeeRequest = {}  # type: ignore[typeddict-item]
    return out
