"""Generated from Smithy shape ``com.amazonaws.sustainability#DimensionEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.dimension_entry

DimensionEntryList: TypeAlias = list[
    "aws_sdk_sustainability.types.dimension_entry.DimensionEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionEntryList) -> list:
    import aws_sdk_sustainability.types.dimension_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_sustainability.types.dimension_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> DimensionEntryList:
    import aws_sdk_sustainability.types.dimension_entry

    out: DimensionEntryList = []
    for item in data:
        out.append(aws_sdk_sustainability.types.dimension_entry.deserialize_json(item))
    return out
