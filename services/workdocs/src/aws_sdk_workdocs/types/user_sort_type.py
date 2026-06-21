"""Generated from Smithy shape ``com.amazonaws.workdocs#UserSortType``."""

from typing import Literal, TypeAlias, cast

UserSortType: TypeAlias = Literal[
    "USER_NAME",
    "FULL_NAME",
    "STORAGE_LIMIT",
    "USER_STATUS",
    "STORAGE_USED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserSortType) -> str:
    return value


def deserialize_json(data: str) -> UserSortType:
    return cast(UserSortType, data)
