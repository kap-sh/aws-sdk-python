"""Generated from Smithy shape ``com.amazonaws.quicksight#CollectiveConstantEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.collective_constant_entry

CollectiveConstantEntryList: TypeAlias = list[
    "aws_sdk_quicksight.types.collective_constant_entry.CollectiveConstantEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollectiveConstantEntryList) -> list:
    import aws_sdk_quicksight.types.collective_constant_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.collective_constant_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CollectiveConstantEntryList:
    import aws_sdk_quicksight.types.collective_constant_entry

    out: CollectiveConstantEntryList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.collective_constant_entry.deserialize_json(item)
        )
    return out
