"""Generated from Smithy shape ``com.amazonaws.iotwireless#ApplicationConfigType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

ApplicationConfigType: TypeAlias = Literal["SemtechGeolocation",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SemtechGeolocation",))


def serialize_json(value: ApplicationConfigType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationConfigType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationConfigType value: {data!r}")
    return cast(ApplicationConfigType, data)
