"""Generated from Smithy shape ``com.amazonaws.outposts#UplinkCount``."""

from typing import Literal, TypeAlias, cast

UplinkCount: TypeAlias = Literal[
    "UPLINK_COUNT_1",
    "UPLINK_COUNT_2",
    "UPLINK_COUNT_3",
    "UPLINK_COUNT_4",
    "UPLINK_COUNT_5",
    "UPLINK_COUNT_6",
    "UPLINK_COUNT_7",
    "UPLINK_COUNT_8",
    "UPLINK_COUNT_12",
    "UPLINK_COUNT_16",
]


# --- restJson1 ser/de ---
def serialize_json(value: UplinkCount) -> str:
    return value


def deserialize_json(data: str) -> UplinkCount:
    return cast(UplinkCount, data)
