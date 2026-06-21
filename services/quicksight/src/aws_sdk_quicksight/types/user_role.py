"""Generated from Smithy shape ``com.amazonaws.quicksight#UserRole``."""

from typing import Literal, TypeAlias, cast

UserRole: TypeAlias = Literal[
    "ADMIN",
    "AUTHOR",
    "READER",
    "RESTRICTED_AUTHOR",
    "RESTRICTED_READER",
    "ADMIN_PRO",
    "AUTHOR_PRO",
    "READER_PRO",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserRole) -> str:
    return value


def deserialize_json(data: str) -> UserRole:
    return cast(UserRole, data)
