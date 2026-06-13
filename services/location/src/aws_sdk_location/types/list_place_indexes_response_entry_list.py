"""Generated from Smithy shape ``com.amazonaws.location#ListPlaceIndexesResponseEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.list_place_indexes_response_entry

ListPlaceIndexesResponseEntryList: TypeAlias = list[
    "aws_sdk_location.types.list_place_indexes_response_entry.ListPlaceIndexesResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaceIndexesResponseEntryList) -> list:
    import aws_sdk_location.types.list_place_indexes_response_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_location.types.list_place_indexes_response_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListPlaceIndexesResponseEntryList:
    import aws_sdk_location.types.list_place_indexes_response_entry

    out: ListPlaceIndexesResponseEntryList = []
    for item in data:
        out.append(
            aws_sdk_location.types.list_place_indexes_response_entry.deserialize_json(
                item
            )
        )
    return out
