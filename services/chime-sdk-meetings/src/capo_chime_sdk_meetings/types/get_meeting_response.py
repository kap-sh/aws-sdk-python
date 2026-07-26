"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#GetMeetingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.meeting


class GetMeetingResponse(TypedDict, closed=True):
    meeting: NotRequired["capo_chime_sdk_meetings.types.meeting.Meeting"]
    """<p>The Amazon Chime SDK meeting information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMeetingResponse) -> dict:
    out: dict = {}
    if "meeting" in value:
        import capo_chime_sdk_meetings.types.meeting

        out["Meeting"] = capo_chime_sdk_meetings.types.meeting.serialize_json(
            value["meeting"]
        )
    return out


def deserialize_json(data: dict) -> GetMeetingResponse:
    out: GetMeetingResponse = {}  # type: ignore[typeddict-item]
    if "Meeting" in data:
        import capo_chime_sdk_meetings.types.meeting

        out["meeting"] = capo_chime_sdk_meetings.types.meeting.deserialize_json(
            data["Meeting"]
        )
    return out
