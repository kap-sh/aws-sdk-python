"""Generated from Smithy shape ``com.amazonaws.datazone#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

EntityType: TypeAlias = Literal[
    "ASSET",
    "DATA_PRODUCT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET",
        "DATA_PRODUCT",
    )
)


def serialize_json(value: EntityType) -> str:
    return value


def deserialize_json(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
