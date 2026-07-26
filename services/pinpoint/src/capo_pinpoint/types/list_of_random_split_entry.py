"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfRandomSplitEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.random_split_entry

ListOfRandomSplitEntry: TypeAlias = list[
    "capo_pinpoint.types.random_split_entry.RandomSplitEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRandomSplitEntry) -> list:
    import capo_pinpoint.types.random_split_entry

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.random_split_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfRandomSplitEntry:
    import capo_pinpoint.types.random_split_entry

    out: ListOfRandomSplitEntry = []
    for item in data:
        out.append(capo_pinpoint.types.random_split_entry.deserialize_json(item))
    return out
