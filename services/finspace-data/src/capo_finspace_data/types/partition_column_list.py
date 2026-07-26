"""Generated from Smithy shape ``com.amazonaws.finspacedata#PartitionColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace_data.types.string_value_length1to255

PartitionColumnList: TypeAlias = list[
    "capo_finspace_data.types.string_value_length1to255.StringValueLength1to255"
]


# --- restJson1 ser/de ---
def serialize_json(value: PartitionColumnList) -> list:
    return list(value)


def deserialize_json(data: list) -> PartitionColumnList:
    return list(data)
