"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileStatus``."""

from typing import Literal, TypeAlias, cast

UserProfileStatus: TypeAlias = Literal[
    "ASSIGNED",
    "NOT_ASSIGNED",
    "ACTIVATED",
    "DEACTIVATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> UserProfileStatus:
    return cast(UserProfileStatus, data)
