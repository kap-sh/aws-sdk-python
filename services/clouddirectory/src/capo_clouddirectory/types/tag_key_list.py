"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.tag_key

TagKeyList: TypeAlias = list["capo_clouddirectory.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeyList:
    return list(data)
