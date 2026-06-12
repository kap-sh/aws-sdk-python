"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.search_text_result_item

SearchTextResultItemList: TypeAlias = list[
    "aws_sdk_geo_places.types.search_text_result_item.SearchTextResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextResultItemList) -> list:
    import aws_sdk_geo_places.types.search_text_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_places.types.search_text_result_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchTextResultItemList:
    import aws_sdk_geo_places.types.search_text_result_item

    out: SearchTextResultItemList = []
    for item in data:
        out.append(
            aws_sdk_geo_places.types.search_text_result_item.deserialize_json(item)
        )
    return out
