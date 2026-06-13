"""Generated from Smithy shape ``com.amazonaws.datazone#SearchInList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.search_in_item

SearchInList: TypeAlias = list["aws_sdk_datazone.types.search_in_item.SearchInItem"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchInList) -> list:
    import aws_sdk_datazone.types.search_in_item

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.search_in_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchInList:
    import aws_sdk_datazone.types.search_in_item

    out: SearchInList = []
    for item in data:
        out.append(aws_sdk_datazone.types.search_in_item.deserialize_json(item))
    return out
