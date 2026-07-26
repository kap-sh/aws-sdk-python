"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_field_option

PivotTableFieldOptionList: TypeAlias = list[
    "capo_quicksight.types.pivot_table_field_option.PivotTableFieldOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldOptionList) -> list:
    import capo_quicksight.types.pivot_table_field_option

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.pivot_table_field_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> PivotTableFieldOptionList:
    import capo_quicksight.types.pivot_table_field_option

    out: PivotTableFieldOptionList = []
    for item in data:
        out.append(
            capo_quicksight.types.pivot_table_field_option.deserialize_json(item)
        )
    return out
