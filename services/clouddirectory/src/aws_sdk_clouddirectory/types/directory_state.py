"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DirectoryState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

DirectoryState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "DELETED",
    )
)


def serialize_json(value: DirectoryState) -> str:
    return value


def deserialize_json(data: str) -> DirectoryState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DirectoryState value: {data!r}")
    return cast(DirectoryState, data)
