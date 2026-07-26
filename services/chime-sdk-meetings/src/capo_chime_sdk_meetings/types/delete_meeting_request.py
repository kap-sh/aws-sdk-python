"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#DeleteMeetingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.guid_string


class DeleteMeetingRequest(TypedDict, closed=True):
    meeting_id: "capo_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK meeting ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMeetingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMeetingRequest:
    out: DeleteMeetingRequest = {}  # type: ignore[typeddict-item]
    return out
