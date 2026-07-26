"""Generated from Smithy shape ``com.amazonaws.quicksight#TransposedTableOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.transposed_table_option

TransposedTableOptionList: TypeAlias = list[
    "capo_quicksight.types.transposed_table_option.TransposedTableOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransposedTableOptionList) -> list:
    import capo_quicksight.types.transposed_table_option

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.transposed_table_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> TransposedTableOptionList:
    import capo_quicksight.types.transposed_table_option

    out: TransposedTableOptionList = []
    for item in data:
        out.append(capo_quicksight.types.transposed_table_option.deserialize_json(item))
    return out
