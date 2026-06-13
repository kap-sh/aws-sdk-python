"""Generated from Smithy shape ``com.amazonaws.location#ListTrackersResponseEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.list_trackers_response_entry

ListTrackersResponseEntryList: TypeAlias = list[
    "aws_sdk_location.types.list_trackers_response_entry.ListTrackersResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTrackersResponseEntryList) -> list:
    import aws_sdk_location.types.list_trackers_response_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_location.types.list_trackers_response_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListTrackersResponseEntryList:
    import aws_sdk_location.types.list_trackers_response_entry

    out: ListTrackersResponseEntryList = []
    for item in data:
        out.append(
            aws_sdk_location.types.list_trackers_response_entry.deserialize_json(item)
        )
    return out
