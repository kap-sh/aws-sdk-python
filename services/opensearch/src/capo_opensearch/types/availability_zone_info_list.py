"""Generated from Smithy shape ``com.amazonaws.opensearch#AvailabilityZoneInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.availability_zone_info

AvailabilityZoneInfoList: TypeAlias = list[
    "capo_opensearch.types.availability_zone_info.AvailabilityZoneInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZoneInfoList) -> list:
    import capo_opensearch.types.availability_zone_info

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.availability_zone_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AvailabilityZoneInfoList:
    import capo_opensearch.types.availability_zone_info

    out: AvailabilityZoneInfoList = []
    for item in data:
        out.append(capo_opensearch.types.availability_zone_info.deserialize_json(item))
    return out
