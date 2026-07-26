"""Generated from Smithy shape ``com.amazonaws.inspector2#TagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.target_resource_tags_value

TagValueList: TypeAlias = list[
    "capo_inspector2.types.target_resource_tags_value.TargetResourceTagsValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagValueList:
    return list(data)
