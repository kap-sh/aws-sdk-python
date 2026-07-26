"""Generated from Smithy shape ``com.amazonaws.backupsearch#ResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backupsearch.types.resource_type

ResourceTypeList: TypeAlias = list["capo_backupsearch.types.resource_type.ResourceType"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeList) -> list:
    import capo_backupsearch.types.resource_type

    out: list = []
    for item in value:
        out.append(capo_backupsearch.types.resource_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTypeList:
    import capo_backupsearch.types.resource_type

    out: ResourceTypeList = []
    for item in data:
        out.append(capo_backupsearch.types.resource_type.deserialize_json(item))
    return out
