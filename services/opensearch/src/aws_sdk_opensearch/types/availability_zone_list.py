"""Generated from Smithy shape ``com.amazonaws.opensearch#AvailabilityZoneList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.availability_zone

AvailabilityZoneList: TypeAlias = list[
    "aws_sdk_opensearch.types.availability_zone.AvailabilityZone"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZoneList) -> list:
    return list(value)


def deserialize_json(data: list) -> AvailabilityZoneList:
    return list(data)
