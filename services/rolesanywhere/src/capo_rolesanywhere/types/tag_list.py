"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rolesanywhere.types.tag

TagList: TypeAlias = list["capo_rolesanywhere.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagList) -> list:
    import capo_rolesanywhere.types.tag

    out: list = []
    for item in value:
        out.append(capo_rolesanywhere.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagList:
    import capo_rolesanywhere.types.tag

    out: TagList = []
    for item in data:
        out.append(capo_rolesanywhere.types.tag.deserialize_json(item))
    return out
