"""Generated from Smithy shape ``com.amazonaws.securityhub#AvailabilityZones``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.availability_zone

AvailabilityZones: TypeAlias = list[
    "capo_securityhub.types.availability_zone.AvailabilityZone"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZones) -> list:
    import capo_securityhub.types.availability_zone

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.availability_zone.serialize_json(item))
    return out


def deserialize_json(data: list) -> AvailabilityZones:
    import capo_securityhub.types.availability_zone

    out: AvailabilityZones = []
    for item in data:
        out.append(capo_securityhub.types.availability_zone.deserialize_json(item))
    return out
