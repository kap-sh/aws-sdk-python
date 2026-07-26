"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProtocolType``."""

from typing import Literal, TypeAlias, cast

ProtocolType: TypeAlias = Literal[
    "ZWAVE",
    "ZIGBEE",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtocolType) -> str:
    return value


def deserialize_json(data: str) -> ProtocolType:
    return cast(ProtocolType, data)
