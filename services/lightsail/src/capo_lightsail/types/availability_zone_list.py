"""Generated from Smithy shape ``com.amazonaws.lightsail#AvailabilityZoneList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.availability_zone

AvailabilityZoneList: TypeAlias = list[
    "capo_lightsail.types.availability_zone.AvailabilityZone"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityZoneList) -> list:
    import capo_lightsail.types.availability_zone

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.availability_zone.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AvailabilityZoneList:
    import capo_lightsail.types.availability_zone

    out: AvailabilityZoneList = []
    for item in data:
        out.append(
            capo_lightsail.types.availability_zone.deserialize_aws_json_1_1(item)
        )
    return out
