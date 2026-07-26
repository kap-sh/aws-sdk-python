"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#MemberType``."""

from typing import Literal, TypeAlias, cast

MemberType: TypeAlias = Literal[
    "USER",
    "GROUP",
    "COMPUTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberType) -> str:
    return value


def deserialize_json(data: str) -> MemberType:
    return cast(MemberType, data)
