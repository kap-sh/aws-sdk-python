"""Generated from Smithy shape ``com.amazonaws.chime#UpdateRoomResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.room


class UpdateRoomResponse(TypedDict, closed=True):
    room: NotRequired["capo_chime.types.room.Room"]
    """<p>The room details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoomResponse) -> dict:
    out: dict = {}
    if "room" in value:
        import capo_chime.types.room

        out["Room"] = capo_chime.types.room.serialize_json(value["room"])
    return out


def deserialize_json(data: dict) -> UpdateRoomResponse:
    out: UpdateRoomResponse = {}  # type: ignore[typeddict-item]
    if "Room" in data:
        import capo_chime.types.room

        out["room"] = capo_chime.types.room.deserialize_json(data["Room"])
    return out
