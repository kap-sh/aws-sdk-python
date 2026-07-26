"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionResourceType``."""

from typing import Literal, TypeAlias, cast

PositionResourceType: TypeAlias = Literal[
    "WirelessDevice",
    "WirelessGateway",
]


# --- restJson1 ser/de ---
def serialize_json(value: PositionResourceType) -> str:
    return value


def deserialize_json(data: str) -> PositionResourceType:
    return cast(PositionResourceType, data)
