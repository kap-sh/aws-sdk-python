"""Generated from Smithy shape ``com.amazonaws.devopsguru#TagCollections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.tag_collection

TagCollections: TypeAlias = list["capo_devops_guru.types.tag_collection.TagCollection"]


# --- restJson1 ser/de ---
def serialize_json(value: TagCollections) -> list:
    import capo_devops_guru.types.tag_collection

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.tag_collection.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagCollections:
    import capo_devops_guru.types.tag_collection

    out: TagCollections = []
    for item in data:
        out.append(capo_devops_guru.types.tag_collection.deserialize_json(item))
    return out
