"""Generated from Smithy shape ``com.amazonaws.finspacedata#UserType``."""

from typing import Literal, TypeAlias, cast

UserType: TypeAlias = Literal[
    "SUPER_USER",
    "APP_USER",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    return cast(UserType, data)
