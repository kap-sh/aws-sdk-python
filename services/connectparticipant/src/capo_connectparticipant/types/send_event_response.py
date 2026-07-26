"""Generated from Smithy shape ``com.amazonaws.connectparticipant#SendEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.chat_item_id
    import capo_connectparticipant.types.instant


class SendEventResponse(TypedDict, closed=True):
    id: NotRequired["capo_connectparticipant.types.chat_item_id.ChatItemId"]
    """<p>The ID of the response.</p>"""
    absolute_time: NotRequired["capo_connectparticipant.types.instant.Instant"]
    """<p>The time when the event was sent.</p> <p>It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendEventResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "absolute_time" in value:
        out["AbsoluteTime"] = value["absolute_time"]
    return out


def deserialize_json(data: dict) -> SendEventResponse:
    out: SendEventResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "AbsoluteTime" in data:
        out["absolute_time"] = data["AbsoluteTime"]
    return out
