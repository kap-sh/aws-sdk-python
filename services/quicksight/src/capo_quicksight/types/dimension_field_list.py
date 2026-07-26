"""Generated from Smithy shape ``com.amazonaws.quicksight#DimensionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field

DimensionFieldList: TypeAlias = list[
    "capo_quicksight.types.dimension_field.DimensionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionFieldList) -> list:
    import capo_quicksight.types.dimension_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.dimension_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> DimensionFieldList:
    import capo_quicksight.types.dimension_field

    out: DimensionFieldList = []
    for item in data:
        out.append(capo_quicksight.types.dimension_field.deserialize_json(item))
    return out
