"""Generated from Smithy shape ``com.amazonaws.chime#RoomMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.room_membership

RoomMembershipList: TypeAlias = list["capo_chime.types.room_membership.RoomMembership"]


# --- restJson1 ser/de ---
def serialize_json(value: RoomMembershipList) -> list:
    import capo_chime.types.room_membership

    out: list = []
    for item in value:
        out.append(capo_chime.types.room_membership.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoomMembershipList:
    import capo_chime.types.room_membership

    out: RoomMembershipList = []
    for item in data:
        out.append(capo_chime.types.room_membership.deserialize_json(item))
    return out
