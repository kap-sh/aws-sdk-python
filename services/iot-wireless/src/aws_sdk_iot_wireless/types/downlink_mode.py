"""Generated from Smithy shape ``com.amazonaws.iotwireless#DownlinkMode``."""

from typing import Literal, TypeAlias, cast

DownlinkMode: TypeAlias = Literal[
    "SEQUENTIAL",
    "CONCURRENT",
    "USING_UPLINK_GATEWAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkMode) -> str:
    return value


def deserialize_json(data: str) -> DownlinkMode:
    return cast(DownlinkMode, data)
