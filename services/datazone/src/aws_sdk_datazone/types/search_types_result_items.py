"""Generated from Smithy shape ``com.amazonaws.datazone#SearchTypesResultItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.search_types_result_item

SearchTypesResultItems: TypeAlias = list[
    "aws_sdk_datazone.types.search_types_result_item.SearchTypesResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTypesResultItems) -> list:
    import aws_sdk_datazone.types.search_types_result_item

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.search_types_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchTypesResultItems:
    import aws_sdk_datazone.types.search_types_result_item

    out: SearchTypesResultItems = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.search_types_result_item.deserialize_json(item)
        )
    return out
