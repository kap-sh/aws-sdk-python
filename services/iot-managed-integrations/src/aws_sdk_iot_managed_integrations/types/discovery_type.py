"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveryType``."""

from typing import Literal, TypeAlias, cast

DiscoveryType: TypeAlias = Literal[
    "ZWAVE",
    "ZIGBEE",
    "CLOUD",
    "CUSTOM",
    "CONTROLLER_CAPABILITY_REDISCOVERY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryType) -> str:
    return value


def deserialize_json(data: str) -> DiscoveryType:
    return cast(DiscoveryType, data)
