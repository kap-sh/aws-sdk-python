"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceTagFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.tag_filter

ResourceTagFilterList: TypeAlias = list["aws_sdk_inspector2.types.tag_filter.TagFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTagFilterList) -> list:
    import aws_sdk_inspector2.types.tag_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.tag_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTagFilterList:
    import aws_sdk_inspector2.types.tag_filter

    out: ResourceTagFilterList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.tag_filter.deserialize_json(item))
    return out
