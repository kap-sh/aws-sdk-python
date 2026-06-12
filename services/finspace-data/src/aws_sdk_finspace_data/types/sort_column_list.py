"""Generated from Smithy shape ``com.amazonaws.finspacedata#SortColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.string_value_length1to255

SortColumnList: TypeAlias = list[
    "aws_sdk_finspace_data.types.string_value_length1to255.StringValueLength1to255"
]


# --- restJson1 ser/de ---
def serialize_json(value: SortColumnList) -> list:
    return list(value)


def deserialize_json(data: list) -> SortColumnList:
    return list(data)
