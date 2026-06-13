"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#RegionStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.region_status

RegionStatusList: TypeAlias = list[
    "aws_sdk_resource_explorer_2.types.region_status.RegionStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegionStatusList) -> list:
    import aws_sdk_resource_explorer_2.types.region_status

    out: list = []
    for item in value:
        out.append(aws_sdk_resource_explorer_2.types.region_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> RegionStatusList:
    import aws_sdk_resource_explorer_2.types.region_status

    out: RegionStatusList = []
    for item in data:
        out.append(
            aws_sdk_resource_explorer_2.types.region_status.deserialize_json(item)
        )
    return out
