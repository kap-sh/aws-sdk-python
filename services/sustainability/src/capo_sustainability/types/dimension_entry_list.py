"""Generated from Smithy shape ``com.amazonaws.sustainability#DimensionEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sustainability.types.dimension_entry

DimensionEntryList: TypeAlias = list[
    "capo_sustainability.types.dimension_entry.DimensionEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionEntryList) -> list:
    import capo_sustainability.types.dimension_entry

    out: list = []
    for item in value:
        out.append(capo_sustainability.types.dimension_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> DimensionEntryList:
    import capo_sustainability.types.dimension_entry

    out: DimensionEntryList = []
    for item in data:
        out.append(capo_sustainability.types.dimension_entry.deserialize_json(item))
    return out
