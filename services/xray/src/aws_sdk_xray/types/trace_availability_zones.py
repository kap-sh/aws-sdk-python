"""Generated from Smithy shape ``com.amazonaws.xray#TraceAvailabilityZones``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.availability_zone_detail

TraceAvailabilityZones: TypeAlias = list[
    "aws_sdk_xray.types.availability_zone_detail.AvailabilityZoneDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: TraceAvailabilityZones) -> list:
    import aws_sdk_xray.types.availability_zone_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.availability_zone_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> TraceAvailabilityZones:
    import aws_sdk_xray.types.availability_zone_detail

    out: TraceAvailabilityZones = []
    for item in data:
        out.append(aws_sdk_xray.types.availability_zone_detail.deserialize_json(item))
    return out
