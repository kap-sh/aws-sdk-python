"""Generated from Smithy shape ``com.amazonaws.finspace#AvailabilityZoneIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.availability_zone_id

AvailabilityZoneIds: TypeAlias = list[
    "capo_finspace.types.availability_zone_id.AvailabilityZoneId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZoneIds) -> list:
    return list(value)


def deserialize_json(data: list) -> AvailabilityZoneIds:
    return list(data)
