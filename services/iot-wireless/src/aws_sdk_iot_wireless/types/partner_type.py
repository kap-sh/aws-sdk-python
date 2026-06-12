"""Generated from Smithy shape ``com.amazonaws.iotwireless#PartnerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

PartnerType: TypeAlias = Literal["Sidewalk",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Sidewalk",))


def serialize_json(value: PartnerType) -> str:
    return value


def deserialize_json(data: str) -> PartnerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PartnerType value: {data!r}")
    return cast(PartnerType, data)
