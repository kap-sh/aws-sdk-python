"""Generated from Smithy shape ``com.amazonaws.rbin#ExcludeResourceTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rbin.types.resource_tag

ExcludeResourceTags: TypeAlias = list["capo_rbin.types.resource_tag.ResourceTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ExcludeResourceTags) -> list:
    import capo_rbin.types.resource_tag

    out: list = []
    for item in value:
        out.append(capo_rbin.types.resource_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExcludeResourceTags:
    import capo_rbin.types.resource_tag

    out: ExcludeResourceTags = []
    for item in data:
        out.append(capo_rbin.types.resource_tag.deserialize_json(item))
    return out
