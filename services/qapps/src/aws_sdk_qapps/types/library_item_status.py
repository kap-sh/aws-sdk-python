"""Generated from Smithy shape ``com.amazonaws.qapps#LibraryItemStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

LibraryItemStatus: TypeAlias = Literal[
    "PUBLISHED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISHED",
        "DISABLED",
    )
)


def serialize_json(value: LibraryItemStatus) -> str:
    return value


def deserialize_json(data: str) -> LibraryItemStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LibraryItemStatus value: {data!r}")
    return cast(LibraryItemStatus, data)
