"""Generated from Smithy shape ``com.amazonaws.macie2#SharedAccess``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

SharedAccess: TypeAlias = Literal[
    "EXTERNAL",
    "INTERNAL",
    "NOT_SHARED",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXTERNAL",
        "INTERNAL",
        "NOT_SHARED",
        "UNKNOWN",
    )
)


def serialize_json(value: SharedAccess) -> str:
    return value


def deserialize_json(data: str) -> SharedAccess:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SharedAccess value: {data!r}")
    return cast(SharedAccess, data)
