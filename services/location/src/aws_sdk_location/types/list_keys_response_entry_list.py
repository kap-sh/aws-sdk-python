"""Generated from Smithy shape ``com.amazonaws.location#ListKeysResponseEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.list_keys_response_entry

ListKeysResponseEntryList: TypeAlias = list[
    "aws_sdk_location.types.list_keys_response_entry.ListKeysResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListKeysResponseEntryList) -> list:
    import aws_sdk_location.types.list_keys_response_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.list_keys_response_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListKeysResponseEntryList:
    import aws_sdk_location.types.list_keys_response_entry

    out: ListKeysResponseEntryList = []
    for item in data:
        out.append(
            aws_sdk_location.types.list_keys_response_entry.deserialize_json(item)
        )
    return out
