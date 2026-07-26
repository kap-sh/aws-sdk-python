"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.resource_type

ResourceTypeList: TypeAlias = list[
    "capo_accessanalyzer.types.resource_type.ResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceTypeList:
    return list(data)
