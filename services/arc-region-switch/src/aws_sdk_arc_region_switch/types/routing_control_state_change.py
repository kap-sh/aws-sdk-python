"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RoutingControlStateChange``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

RoutingControlStateChange: TypeAlias = Literal[
    "On",
    "Off",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "On",
        "Off",
    )
)


def serialize_aws_json_1_0(value: RoutingControlStateChange) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RoutingControlStateChange:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingControlStateChange value: {data!r}")
    return cast(RoutingControlStateChange, data)
