"""Generated from Smithy shape ``com.amazonaws.connect#DeviceType``."""

from typing import Literal, TypeAlias, cast

DeviceType: TypeAlias = Literal[
    "GCM",
    "APNS",
    "APNS_SANDBOX",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceType) -> str:
    return value


def deserialize_json(data: str) -> DeviceType:
    return cast(DeviceType, data)
