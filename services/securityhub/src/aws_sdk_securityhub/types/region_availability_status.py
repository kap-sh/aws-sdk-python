"""Generated from Smithy shape ``com.amazonaws.securityhub#RegionAvailabilityStatus``."""

from typing import Literal, TypeAlias, cast

RegionAvailabilityStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegionAvailabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> RegionAvailabilityStatus:
    return cast(RegionAvailabilityStatus, data)
