"""Generated from Smithy shape ``com.amazonaws.datazone#SearchResultItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.search_result_item

SearchResultItems: TypeAlias = list[
    "aws_sdk_datazone.types.search_result_item.SearchResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultItems) -> list:
    import aws_sdk_datazone.types.search_result_item

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.search_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchResultItems:
    import aws_sdk_datazone.types.search_result_item

    out: SearchResultItems = []
    for item in data:
        out.append(aws_sdk_datazone.types.search_result_item.deserialize_json(item))
    return out
