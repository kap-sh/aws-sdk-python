"""Generated from Smithy shape ``com.amazonaws.connectparticipant#Attendee``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.attendee_id
    import capo_connectparticipant.types.join_token


class Attendee(TypedDict, closed=True):
    attendee_id: NotRequired["capo_connectparticipant.types.attendee_id.AttendeeId"]
    """<p>The Amazon Chime SDK attendee ID.</p>"""
    join_token: NotRequired["capo_connectparticipant.types.join_token.JoinToken"]
    """<p>The join token used by the Amazon Chime SDK attendee.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attendee) -> dict:
    out: dict = {}
    if "attendee_id" in value:
        out["AttendeeId"] = value["attendee_id"]
    if "join_token" in value:
        out["JoinToken"] = value["join_token"]
    return out


def deserialize_json(data: dict) -> Attendee:
    out: Attendee = {}  # type: ignore[typeddict-item]
    if "AttendeeId" in data:
        out["attendee_id"] = data["AttendeeId"]
    if "JoinToken" in data:
        out["join_token"] = data["JoinToken"]
    return out
