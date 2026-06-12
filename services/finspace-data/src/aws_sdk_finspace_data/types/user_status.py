"""Generated from Smithy shape ``com.amazonaws.finspacedata#UserStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

UserStatus: TypeAlias = Literal[
    "CREATING",
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: UserStatus) -> str:
    return value


def deserialize_json(data: str) -> UserStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserStatus value: {data!r}")
    return cast(UserStatus, data)
