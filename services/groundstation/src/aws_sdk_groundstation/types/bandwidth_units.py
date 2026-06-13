"""Generated from Smithy shape ``com.amazonaws.groundstation#BandwidthUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

BandwidthUnits: TypeAlias = Literal[
    "GHz",
    "MHz",
    "kHz",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GHz",
        "MHz",
        "kHz",
    )
)


def serialize_json(value: BandwidthUnits) -> str:
    return value


def deserialize_json(data: str) -> BandwidthUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BandwidthUnits value: {data!r}")
    return cast(BandwidthUnits, data)
