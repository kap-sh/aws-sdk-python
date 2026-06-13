"""Generated from Smithy shape ``com.amazonaws.quicksight#Role``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

Role: TypeAlias = Literal[
    "ADMIN",
    "AUTHOR",
    "READER",
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
        "ADMIN_PRO",
        "AUTHOR_PRO",
        "READER_PRO",
    )
)


def serialize_json(value: Role) -> str:
    return value


def deserialize_json(data: str) -> Role:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Role value: {data!r}")
    return cast(Role, data)
