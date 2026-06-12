"""Generated from Smithy shape ``com.amazonaws.chime#RoomList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.room

RoomList: TypeAlias = list["aws_sdk_chime.types.room.Room"]


# --- restJson1 ser/de ---
def serialize_json(value: RoomList) -> list:
    import aws_sdk_chime.types.room

    out: list = []
    for item in value:
        out.append(aws_sdk_chime.types.room.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoomList:
    import aws_sdk_chime.types.room

    out: RoomList = []
    for item in data:
        out.append(aws_sdk_chime.types.room.deserialize_json(item))
    return out
