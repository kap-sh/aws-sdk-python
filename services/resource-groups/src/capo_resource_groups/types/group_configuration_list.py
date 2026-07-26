"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups.types.group_configuration_item

GroupConfigurationList: TypeAlias = list[
    "capo_resource_groups.types.group_configuration_item.GroupConfigurationItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupConfigurationList) -> list:
    import capo_resource_groups.types.group_configuration_item

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups.types.group_configuration_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GroupConfigurationList:
    import capo_resource_groups.types.group_configuration_item

    out: GroupConfigurationList = []
    for item in data:
        out.append(
            capo_resource_groups.types.group_configuration_item.deserialize_json(item)
        )
    return out
