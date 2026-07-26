"""Generated from Smithy shape ``com.amazonaws.datazone#ResourceTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.resource_tag

ResourceTags: TypeAlias = list["capo_datazone.types.resource_tag.ResourceTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTags) -> list:
    import capo_datazone.types.resource_tag

    out: list = []
    for item in value:
        out.append(capo_datazone.types.resource_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTags:
    import capo_datazone.types.resource_tag

    out: ResourceTags = []
    for item in data:
        out.append(capo_datazone.types.resource_tag.deserialize_json(item))
    return out
