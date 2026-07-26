"""Generated from Smithy shape ``com.amazonaws.ivschat#RoomList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivschat.types.room_summary

RoomList: TypeAlias = list["capo_ivschat.types.room_summary.RoomSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: RoomList) -> list:
    import capo_ivschat.types.room_summary

    out: list = []
    for item in value:
        out.append(capo_ivschat.types.room_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoomList:
    import capo_ivschat.types.room_summary

    out: RoomList = []
    for item in data:
        out.append(capo_ivschat.types.room_summary.deserialize_json(item))
    return out
