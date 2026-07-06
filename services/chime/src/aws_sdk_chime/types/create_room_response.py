"""Generated from Smithy shape ``com.amazonaws.chime#CreateRoomResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.room


class CreateRoomResponse(TypedDict, closed=True):
    room: NotRequired["aws_sdk_chime.types.room.Room"]
    """<p>The room details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoomResponse) -> dict:
    out: dict = {}
    if "room" in value:
        import aws_sdk_chime.types.room

        out["Room"] = aws_sdk_chime.types.room.serialize_json(value["room"])
    return out


def deserialize_json(data: dict) -> CreateRoomResponse:
    out: CreateRoomResponse = {}  # type: ignore[typeddict-item]
    if "Room" in data:
        import aws_sdk_chime.types.room

        out["room"] = aws_sdk_chime.types.room.deserialize_json(data["Room"])
    return out
