"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35DeviceRestrictions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Corresponds to the device_restrictions parameter in a segmentation_descriptor. If you include one of the \"restriction\" flags then you must include all four of them."""
Scte35DeviceRestrictions: TypeAlias = Literal[
    "NONE",
    "RESTRICT_GROUP0",
    "RESTRICT_GROUP1",
    "RESTRICT_GROUP2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "RESTRICT_GROUP0",
        "RESTRICT_GROUP1",
        "RESTRICT_GROUP2",
    )
)


def serialize_json(value: Scte35DeviceRestrictions) -> str:
    return value


def deserialize_json(data: str) -> Scte35DeviceRestrictions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scte35DeviceRestrictions value: {data!r}")
    return cast(Scte35DeviceRestrictions, data)
