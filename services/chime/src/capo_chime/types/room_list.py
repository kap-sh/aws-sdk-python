"""Generated from Smithy shape ``com.amazonaws.chime#RoomList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.room

RoomList: TypeAlias = list["capo_chime.types.room.Room"]


# --- restJson1 ser/de ---
def serialize_json(value: RoomList) -> list:
    import capo_chime.types.room

    out: list = []
    for item in value:
        out.append(capo_chime.types.room.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoomList:
    import capo_chime.types.room

    out: RoomList = []
    for item in data:
        out.append(capo_chime.types.room.deserialize_json(item))
    return out
