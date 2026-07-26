"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.resource_tag

ResourceTagList: TypeAlias = list["capo_resiliencehubv2.types.resource_tag.ResourceTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTagList) -> list:
    import capo_resiliencehubv2.types.resource_tag

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.resource_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTagList:
    import capo_resiliencehubv2.types.resource_tag

    out: ResourceTagList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.resource_tag.deserialize_json(item))
    return out
