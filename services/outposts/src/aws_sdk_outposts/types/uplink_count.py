"""Generated from Smithy shape ``com.amazonaws.outposts#UplinkCount``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: UplinkCount) -> str:
    return value


def deserialize_json(data: str) -> UplinkCount:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UplinkCount value: {data!r}")
    return cast(UplinkCount, data)
