"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#DeleteMeetingRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.guid_string


class DeleteMeetingRequest(TypedDict):
    meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK meeting ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMeetingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMeetingRequest:
    out: DeleteMeetingRequest = {}  # type: ignore[typeddict-item]
    return out
