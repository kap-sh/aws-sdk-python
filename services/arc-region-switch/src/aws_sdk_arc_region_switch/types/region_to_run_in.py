"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionToRunIn``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

RegionToRunIn: TypeAlias = Literal[
    "activatingRegion",
    "deactivatingRegion",
    "activeRegion",
    "inactiveRegion",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "activatingRegion",
        "deactivatingRegion",
        "activeRegion",
        "inactiveRegion",
    )
)


def serialize_aws_json_1_0(value: RegionToRunIn) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RegionToRunIn:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegionToRunIn value: {data!r}")
    return cast(RegionToRunIn, data)
