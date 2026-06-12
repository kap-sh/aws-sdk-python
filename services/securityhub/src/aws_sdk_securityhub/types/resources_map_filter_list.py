"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesMapFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_map_filter

ResourcesMapFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.resources_map_filter.ResourcesMapFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesMapFilterList) -> list:
    import aws_sdk_securityhub.types.resources_map_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.resources_map_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcesMapFilterList:
    import aws_sdk_securityhub.types.resources_map_filter

    out: ResourcesMapFilterList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.resources_map_filter.deserialize_json(item)
        )
    return out
