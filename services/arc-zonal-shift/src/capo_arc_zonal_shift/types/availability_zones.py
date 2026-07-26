"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AvailabilityZones``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.availability_zone

AvailabilityZones: TypeAlias = list[
    "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZones) -> list:
    return list(value)


def deserialize_json(data: list) -> AvailabilityZones:
    return list(data)
