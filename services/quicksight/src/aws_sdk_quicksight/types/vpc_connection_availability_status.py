"""Generated from Smithy shape ``com.amazonaws.quicksight#VPCConnectionAvailabilityStatus``."""

from typing import Literal, TypeAlias, cast

VPCConnectionAvailabilityStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
    "PARTIALLY_AVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: VPCConnectionAvailabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> VPCConnectionAvailabilityStatus:
    return cast(VPCConnectionAvailabilityStatus, data)
