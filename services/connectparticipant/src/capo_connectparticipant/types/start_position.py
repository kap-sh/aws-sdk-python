"""Generated from Smithy shape ``com.amazonaws.connectparticipant#StartPosition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.chat_item_id
    import capo_connectparticipant.types.instant
    import capo_connectparticipant.types.most_recent


class StartPosition(TypedDict, closed=True):
    id: NotRequired["capo_connectparticipant.types.chat_item_id.ChatItemId"]
    """<p>The ID of the message or event where to start. </p>"""
    absolute_time: NotRequired["capo_connectparticipant.types.instant.Instant"]
    """<p>The time in ISO format where to start.</p> <p>It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""
    most_recent: "capo_connectparticipant.types.most_recent.MostRecent"
    """<p>The start position of the most recent message where you want to start. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPosition) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "absolute_time" in value:
        out["AbsoluteTime"] = value["absolute_time"]
    out["MostRecent"] = value.get("most_recent", 0)
    return out


def deserialize_json(data: dict) -> StartPosition:
    out: StartPosition = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "AbsoluteTime" in data:
        out["absolute_time"] = data["AbsoluteTime"]
    if "MostRecent" in data:
        out["most_recent"] = data["MostRecent"]
    else:
        out["most_recent"] = 0
    return out
