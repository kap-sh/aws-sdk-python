"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ResourcePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.resource_property

ResourcePropertyList: TypeAlias = list[
    "capo_resource_explorer_2.types.resource_property.ResourceProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePropertyList) -> list:
    import capo_resource_explorer_2.types.resource_property

    out: list = []
    for item in value:
        out.append(
            capo_resource_explorer_2.types.resource_property.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourcePropertyList:
    import capo_resource_explorer_2.types.resource_property

    out: ResourcePropertyList = []
    for item in data:
        out.append(
            capo_resource_explorer_2.types.resource_property.deserialize_json(item)
        )
    return out
