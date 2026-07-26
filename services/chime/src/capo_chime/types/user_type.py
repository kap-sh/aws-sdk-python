"""Generated from Smithy shape ``com.amazonaws.chime#UserType``."""

from typing import Literal, TypeAlias, cast

UserType: TypeAlias = Literal[
    "PrivateUser",
    "SharedDevice",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    return cast(UserType, data)
