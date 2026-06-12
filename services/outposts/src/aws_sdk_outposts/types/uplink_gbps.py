"""Generated from Smithy shape ``com.amazonaws.outposts#UplinkGbps``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

UplinkGbps: TypeAlias = Literal[
    "UPLINK_1G",
    "UPLINK_10G",
    "UPLINK_40G",
    "UPLINK_100G",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPLINK_1G",
        "UPLINK_10G",
        "UPLINK_40G",
        "UPLINK_100G",
    )
)


def serialize_json(value: UplinkGbps) -> str:
    return value


def deserialize_json(data: str) -> UplinkGbps:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UplinkGbps value: {data!r}")
    return cast(UplinkGbps, data)
