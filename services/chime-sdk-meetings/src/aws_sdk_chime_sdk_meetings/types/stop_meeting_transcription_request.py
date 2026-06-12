"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#StopMeetingTranscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.guid_string


class StopMeetingTranscriptionRequest(TypedDict):
    meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The unique ID of the meeting for which you stop transcription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopMeetingTranscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopMeetingTranscriptionRequest:
    out: StopMeetingTranscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
