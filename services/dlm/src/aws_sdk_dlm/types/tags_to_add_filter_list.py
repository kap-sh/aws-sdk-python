"""Generated from Smithy shape ``com.amazonaws.dlm#TagsToAddFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.tag_filter

TagsToAddFilterList: TypeAlias = list["aws_sdk_dlm.types.tag_filter.TagFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: TagsToAddFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagsToAddFilterList:
    return list(data)
