"""Generated from Smithy shape ``com.amazonaws.securityhub#AvailabilityZones``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.availability_zone

AvailabilityZones: TypeAlias = list[
    "aws_sdk_securityhub.types.availability_zone.AvailabilityZone"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZones) -> list:
    import aws_sdk_securityhub.types.availability_zone

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.availability_zone.serialize_json(item))
    return out


def deserialize_json(data: list) -> AvailabilityZones:
    import aws_sdk_securityhub.types.availability_zone

    out: AvailabilityZones = []
    for item in data:
        out.append(aws_sdk_securityhub.types.availability_zone.deserialize_json(item))
    return out
