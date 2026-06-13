"""Generated from Smithy shape ``com.amazonaws.quicksight#UserRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ADMIN",
        "AUTHOR",
        "READER",
        "RESTRICTED_AUTHOR",
        "RESTRICTED_READER",
        "ADMIN_PRO",
        "AUTHOR_PRO",
        "READER_PRO",
    )
)


def serialize_json(value: UserRole) -> str:
    return value


def deserialize_json(data: str) -> UserRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserRole value: {data!r}")
    return cast(UserRole, data)
