"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.resource_mapping

ResourceMappingList: TypeAlias = list[
    "capo_resiliencehub.types.resource_mapping.ResourceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceMappingList) -> list:
    import capo_resiliencehub.types.resource_mapping

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.resource_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceMappingList:
    import capo_resiliencehub.types.resource_mapping

    out: ResourceMappingList = []
    for item in data:
        out.append(capo_resiliencehub.types.resource_mapping.deserialize_json(item))
    return out
