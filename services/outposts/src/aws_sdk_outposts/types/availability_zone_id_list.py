"""Generated from Smithy shape ``com.amazonaws.outposts#AvailabilityZoneIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.availability_zone_id

AvailabilityZoneIdList: TypeAlias = list[
    "aws_sdk_outposts.types.availability_zone_id.AvailabilityZoneId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZoneIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AvailabilityZoneIdList:
    return list(data)
