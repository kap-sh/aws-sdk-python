"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableDataPathOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_data_path_option

PivotTableDataPathOptionList: TypeAlias = list[
    "capo_quicksight.types.pivot_table_data_path_option.PivotTableDataPathOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableDataPathOptionList) -> list:
    import capo_quicksight.types.pivot_table_data_path_option

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.pivot_table_data_path_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PivotTableDataPathOptionList:
    import capo_quicksight.types.pivot_table_data_path_option

    out: PivotTableDataPathOptionList = []
    for item in data:
        out.append(
            capo_quicksight.types.pivot_table_data_path_option.deserialize_json(item)
        )
    return out
