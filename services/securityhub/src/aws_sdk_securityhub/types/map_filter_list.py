"""Generated from Smithy shape ``com.amazonaws.securityhub#MapFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.map_filter

MapFilterList: TypeAlias = list["aws_sdk_securityhub.types.map_filter.MapFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: MapFilterList) -> list:
    import aws_sdk_securityhub.types.map_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.map_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> MapFilterList:
    import aws_sdk_securityhub.types.map_filter

    out: MapFilterList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.map_filter.deserialize_json(item))
    return out
