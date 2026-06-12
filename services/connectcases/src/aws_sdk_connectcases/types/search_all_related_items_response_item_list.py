"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsResponseItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.search_all_related_items_response_item

SearchAllRelatedItemsResponseItemList: TypeAlias = list[
    "aws_sdk_connectcases.types.search_all_related_items_response_item.SearchAllRelatedItemsResponseItem | None"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsResponseItemList) -> list:
    import aws_sdk_connectcases.types.search_all_related_items_response_item

    out: list = []
    for item in value:
        if item is None:
            out.append(None)
            continue
        out.append(
            aws_sdk_connectcases.types.search_all_related_items_response_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SearchAllRelatedItemsResponseItemList:
    import aws_sdk_connectcases.types.search_all_related_items_response_item

    out: SearchAllRelatedItemsResponseItemList = []
    for item in data:
        if item is None:
            out.append(None)
            continue
        out.append(
            aws_sdk_connectcases.types.search_all_related_items_response_item.deserialize_json(
                item
            )
        )
    return out
