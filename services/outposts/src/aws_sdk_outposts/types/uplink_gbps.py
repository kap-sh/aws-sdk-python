"""Generated from Smithy shape ``com.amazonaws.outposts#UplinkGbps``."""

from typing import Literal, TypeAlias, cast

UplinkGbps: TypeAlias = Literal[
    "UPLINK_1G",
    "UPLINK_10G",
    "UPLINK_40G",
    "UPLINK_100G",
]


# --- restJson1 ser/de ---
def serialize_json(value: UplinkGbps) -> str:
    return value


def deserialize_json(data: str) -> UplinkGbps:
    return cast(UplinkGbps, data)
