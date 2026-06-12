"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupResourcesItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.list_group_resources_item

ListGroupResourcesItemList: TypeAlias = list[
    "aws_sdk_resource_groups.types.list_group_resources_item.ListGroupResourcesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupResourcesItemList) -> list:
    import aws_sdk_resource_groups.types.list_group_resources_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resource_groups.types.list_group_resources_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListGroupResourcesItemList:
    import aws_sdk_resource_groups.types.list_group_resources_item

    out: ListGroupResourcesItemList = []
    for item in data:
        out.append(
            aws_sdk_resource_groups.types.list_group_resources_item.deserialize_json(
                item
            )
        )
    return out
