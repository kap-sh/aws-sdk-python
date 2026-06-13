"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldIconSetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TableFieldIconSetType: TypeAlias = Literal["LINK",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LINK",))


def serialize_json(value: TableFieldIconSetType) -> str:
    return value


def deserialize_json(data: str) -> TableFieldIconSetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableFieldIconSetType value: {data!r}")
    return cast(TableFieldIconSetType, data)
