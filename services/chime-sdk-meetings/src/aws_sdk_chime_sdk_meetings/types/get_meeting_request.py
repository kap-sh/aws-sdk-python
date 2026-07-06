"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#GetMeetingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.guid_string


class GetMeetingRequest(TypedDict, closed=True):
    meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK meeting ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMeetingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMeetingRequest:
    out: GetMeetingRequest = {}  # type: ignore[typeddict-item]
    return out
