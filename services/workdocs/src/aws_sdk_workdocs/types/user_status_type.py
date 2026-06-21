"""Generated from Smithy shape ``com.amazonaws.workdocs#UserStatusType``."""

from typing import Literal, TypeAlias, cast

UserStatusType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserStatusType) -> str:
    return value


def deserialize_json(data: str) -> UserStatusType:
    return cast(UserStatusType, data)
