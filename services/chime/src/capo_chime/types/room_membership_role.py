"""Generated from Smithy shape ``com.amazonaws.chime#RoomMembershipRole``."""

from typing import Literal, TypeAlias, cast

RoomMembershipRole: TypeAlias = Literal[
    "Administrator",
    "Member",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoomMembershipRole) -> str:
    return value


def deserialize_json(data: str) -> RoomMembershipRole:
    return cast(RoomMembershipRole, data)
