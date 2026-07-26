"""Generated from Smithy shape ``com.amazonaws.appmesh#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.tag_ref

TagList: TypeAlias = list["capo_app_mesh.types.tag_ref.TagRef"]


# --- restJson1 ser/de ---
def serialize_json(value: TagList) -> list:
    import capo_app_mesh.types.tag_ref

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.tag_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagList:
    import capo_app_mesh.types.tag_ref

    out: TagList = []
    for item in data:
        out.append(capo_app_mesh.types.tag_ref.deserialize_json(item))
    return out
