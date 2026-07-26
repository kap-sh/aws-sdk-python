"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldSubtotalOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_field_subtotal_options

PivotTableFieldSubtotalOptionsList: TypeAlias = list[
    "capo_quicksight.types.pivot_table_field_subtotal_options.PivotTableFieldSubtotalOptions"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldSubtotalOptionsList) -> list:
    import capo_quicksight.types.pivot_table_field_subtotal_options

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.pivot_table_field_subtotal_options.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PivotTableFieldSubtotalOptionsList:
    import capo_quicksight.types.pivot_table_field_subtotal_options

    out: PivotTableFieldSubtotalOptionsList = []
    for item in data:
        out.append(
            capo_quicksight.types.pivot_table_field_subtotal_options.deserialize_json(
                item
            )
        )
    return out
