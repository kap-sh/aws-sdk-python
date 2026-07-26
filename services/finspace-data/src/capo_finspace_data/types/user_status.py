"""Generated from Smithy shape ``com.amazonaws.finspacedata#UserStatus``."""

from typing import Literal, TypeAlias, cast

UserStatus: TypeAlias = Literal[
    "CREATING",
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserStatus) -> str:
    return value


def deserialize_json(data: str) -> UserStatus:
    return cast(UserStatus, data)
