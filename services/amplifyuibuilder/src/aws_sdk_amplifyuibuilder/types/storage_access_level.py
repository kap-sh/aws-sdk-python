"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#StorageAccessLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

StorageAccessLevel: TypeAlias = Literal[
    "public",
    "protected",
    "private",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "public",
        "protected",
        "private",
    )
)


def serialize_json(value: StorageAccessLevel) -> str:
    return value


def deserialize_json(data: str) -> StorageAccessLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageAccessLevel value: {data!r}")
    return cast(StorageAccessLevel, data)
