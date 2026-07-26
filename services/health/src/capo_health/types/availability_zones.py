"""Generated from Smithy shape ``com.amazonaws.health#availabilityZones``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.availability_zone

availabilityZones: TypeAlias = list[
    "capo_health.types.availability_zone.availabilityZone"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: availabilityZones) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> availabilityZones:
    return list(data)
