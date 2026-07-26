"""Generated from Smithy shape ``com.amazonaws.dlm#TagsToAddList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.tag

TagsToAddList: TypeAlias = list["capo_dlm.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagsToAddList) -> list:
    import capo_dlm.types.tag

    out: list = []
    for item in value:
        out.append(capo_dlm.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagsToAddList:
    import capo_dlm.types.tag

    out: TagsToAddList = []
    for item in data:
        out.append(capo_dlm.types.tag.deserialize_json(item))
    return out
