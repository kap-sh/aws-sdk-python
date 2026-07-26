"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnToUnpivotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_to_unpivot

ColumnToUnpivotList: TypeAlias = list[
    "capo_quicksight.types.column_to_unpivot.ColumnToUnpivot"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnToUnpivotList) -> list:
    import capo_quicksight.types.column_to_unpivot

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_to_unpivot.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnToUnpivotList:
    import capo_quicksight.types.column_to_unpivot

    out: ColumnToUnpivotList = []
    for item in data:
        out.append(capo_quicksight.types.column_to_unpivot.deserialize_json(item))
    return out
