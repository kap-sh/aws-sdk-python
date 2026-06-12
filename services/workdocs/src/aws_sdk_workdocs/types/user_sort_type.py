"""Generated from Smithy shape ``com.amazonaws.workdocs#UserSortType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

UserSortType: TypeAlias = Literal[
    "USER_NAME",
    "FULL_NAME",
    "STORAGE_LIMIT",
    "USER_STATUS",
    "STORAGE_USED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER_NAME",
        "FULL_NAME",
        "STORAGE_LIMIT",
        "USER_STATUS",
        "STORAGE_USED",
    )
)


def serialize_json(value: UserSortType) -> str:
    return value


def deserialize_json(data: str) -> UserSortType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserSortType value: {data!r}")
    return cast(UserSortType, data)
