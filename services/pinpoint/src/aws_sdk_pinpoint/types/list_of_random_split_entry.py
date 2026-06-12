"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfRandomSplitEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.random_split_entry

ListOfRandomSplitEntry: TypeAlias = list[
    "aws_sdk_pinpoint.types.random_split_entry.RandomSplitEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRandomSplitEntry) -> list:
    import aws_sdk_pinpoint.types.random_split_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.random_split_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfRandomSplitEntry:
    import aws_sdk_pinpoint.types.random_split_entry

    out: ListOfRandomSplitEntry = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.random_split_entry.deserialize_json(item))
    return out
