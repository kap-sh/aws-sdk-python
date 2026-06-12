"""Generated from Smithy shape ``com.amazonaws.mq#__listOfAvailabilityZone``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.availability_zone

__listOfAvailabilityZone: TypeAlias = list[
    "aws_sdk_mq.types.availability_zone.AvailabilityZone"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAvailabilityZone) -> list:
    import aws_sdk_mq.types.availability_zone

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.availability_zone.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAvailabilityZone:
    import aws_sdk_mq.types.availability_zone

    out: __listOfAvailabilityZone = []
    for item in data:
        out.append(aws_sdk_mq.types.availability_zone.deserialize_json(item))
    return out
