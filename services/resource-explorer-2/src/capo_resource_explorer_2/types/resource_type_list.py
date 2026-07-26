"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.supported_resource_type

ResourceTypeList: TypeAlias = list[
    "capo_resource_explorer_2.types.supported_resource_type.SupportedResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeList) -> list:
    import capo_resource_explorer_2.types.supported_resource_type

    out: list = []
    for item in value:
        out.append(
            capo_resource_explorer_2.types.supported_resource_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourceTypeList:
    import capo_resource_explorer_2.types.supported_resource_type

    out: ResourceTypeList = []
    for item in data:
        out.append(
            capo_resource_explorer_2.types.supported_resource_type.deserialize_json(
                item
            )
        )
    return out
