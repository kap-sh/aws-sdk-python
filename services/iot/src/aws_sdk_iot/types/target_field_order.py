"""Generated from Smithy shape ``com.amazonaws.iot#TargetFieldOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

TargetFieldOrder: TypeAlias = Literal[
    "LatLon",
    "LonLat",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LatLon",
        "LonLat",
    )
)


def serialize_json(value: TargetFieldOrder) -> str:
    return value


def deserialize_json(data: str) -> TargetFieldOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetFieldOrder value: {data!r}")
    return cast(TargetFieldOrder, data)
