"""Generated from Smithy shape ``com.amazonaws.dlm#AvailabilityZoneIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.availability_zone_id

AvailabilityZoneIdList: TypeAlias = list[
    "capo_dlm.types.availability_zone_id.AvailabilityZoneId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZoneIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AvailabilityZoneIdList:
    return list(data)
