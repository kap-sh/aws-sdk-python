"""Generated from Smithy shape ``com.amazonaws.dlm#AvailabilityZoneList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.availability_zone

AvailabilityZoneList: TypeAlias = list[
    "capo_dlm.types.availability_zone.AvailabilityZone"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZoneList) -> list:
    return list(value)


def deserialize_json(data: list) -> AvailabilityZoneList:
    return list(data)
