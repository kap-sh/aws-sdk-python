"""Generated from Smithy shape ``com.amazonaws.dlm#TargetTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.tag

TargetTagList: TypeAlias = list["capo_dlm.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TargetTagList) -> list:
    import capo_dlm.types.tag

    out: list = []
    for item in value:
        out.append(capo_dlm.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetTagList:
    import capo_dlm.types.tag

    out: TargetTagList = []
    for item in data:
        out.append(capo_dlm.types.tag.deserialize_json(item))
    return out
