"""Generated from Smithy shape ``com.amazonaws.iotwireless#DimensionName``."""

from typing import Literal, TypeAlias, cast

DimensionName: TypeAlias = Literal[
    "DeviceId",
    "GatewayId",
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionName) -> str:
    return value


def deserialize_json(data: str) -> DimensionName:
    return cast(DimensionName, data)
