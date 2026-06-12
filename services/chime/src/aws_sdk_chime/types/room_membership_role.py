"""Generated from Smithy shape ``com.amazonaws.chime#RoomMembershipRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

RoomMembershipRole: TypeAlias = Literal[
    "Administrator",
    "Member",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Administrator",
        "Member",
    )
)


def serialize_json(value: RoomMembershipRole) -> str:
    return value


def deserialize_json(data: str) -> RoomMembershipRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoomMembershipRole value: {data!r}")
    return cast(RoomMembershipRole, data)
