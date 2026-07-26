"""Generated from Smithy shape ``com.amazonaws.dlm#TargetTagsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.tag_filter

TargetTagsFilterList: TypeAlias = list["capo_dlm.types.tag_filter.TagFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: TargetTagsFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetTagsFilterList:
    return list(data)
