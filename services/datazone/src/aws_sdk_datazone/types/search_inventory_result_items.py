"""Generated from Smithy shape ``com.amazonaws.datazone#SearchInventoryResultItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.search_inventory_result_item

SearchInventoryResultItems: TypeAlias = list[
    "aws_sdk_datazone.types.search_inventory_result_item.SearchInventoryResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchInventoryResultItems) -> list:
    import aws_sdk_datazone.types.search_inventory_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.search_inventory_result_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchInventoryResultItems:
    import aws_sdk_datazone.types.search_inventory_result_item

    out: SearchInventoryResultItems = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.search_inventory_result_item.deserialize_json(item)
        )
    return out
