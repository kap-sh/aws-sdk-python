"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#StopMeetingTranscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.guid_string


class StopMeetingTranscriptionRequest(TypedDict, closed=True):
    meeting_id: "capo_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The unique ID of the meeting for which you stop transcription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopMeetingTranscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopMeetingTranscriptionRequest:
    out: StopMeetingTranscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
