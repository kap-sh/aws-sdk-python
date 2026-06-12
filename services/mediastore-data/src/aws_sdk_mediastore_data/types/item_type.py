"""Generated from Smithy shape ``com.amazonaws.mediastoredata#ItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediastore_data.errors import DeserializationError

ItemType: TypeAlias = Literal[
    "OBJECT",
    "FOLDER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OBJECT",
        "FOLDER",
    )
)


def serialize_json(value: ItemType) -> str:
    return value


def deserialize_json(data: str) -> ItemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ItemType value: {data!r}")
    return cast(ItemType, data)
