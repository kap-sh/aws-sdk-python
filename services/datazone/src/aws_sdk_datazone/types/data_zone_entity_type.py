"""Generated from Smithy shape ``com.amazonaws.datazone#DataZoneEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DataZoneEntityType: TypeAlias = Literal["DOMAIN_UNIT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DOMAIN_UNIT",))


def serialize_json(value: DataZoneEntityType) -> str:
    return value


def deserialize_json(data: str) -> DataZoneEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataZoneEntityType value: {data!r}")
    return cast(DataZoneEntityType, data)
