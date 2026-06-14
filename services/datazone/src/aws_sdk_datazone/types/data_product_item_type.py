"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DataProductItemType: TypeAlias = Literal["ASSET",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ASSET",))


def serialize_json(value: DataProductItemType) -> str:
    return value


def deserialize_json(data: str) -> DataProductItemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataProductItemType value: {data!r}")
    return cast(DataProductItemType, data)
