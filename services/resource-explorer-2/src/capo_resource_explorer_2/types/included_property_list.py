"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#IncludedPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.included_property

IncludedPropertyList: TypeAlias = list[
    "capo_resource_explorer_2.types.included_property.IncludedProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludedPropertyList) -> list:
    import capo_resource_explorer_2.types.included_property

    out: list = []
    for item in value:
        out.append(
            capo_resource_explorer_2.types.included_property.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IncludedPropertyList:
    import capo_resource_explorer_2.types.included_property

    out: IncludedPropertyList = []
    for item in data:
        out.append(
            capo_resource_explorer_2.types.included_property.deserialize_json(item)
        )
    return out
