"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldCollapseStateOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_field_collapse_state_option

PivotTableFieldCollapseStateOptionList: TypeAlias = list[
    "capo_quicksight.types.pivot_table_field_collapse_state_option.PivotTableFieldCollapseStateOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldCollapseStateOptionList) -> list:
    import capo_quicksight.types.pivot_table_field_collapse_state_option

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.pivot_table_field_collapse_state_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PivotTableFieldCollapseStateOptionList:
    import capo_quicksight.types.pivot_table_field_collapse_state_option

    out: PivotTableFieldCollapseStateOptionList = []
    for item in data:
        out.append(
            capo_quicksight.types.pivot_table_field_collapse_state_option.deserialize_json(
                item
            )
        )
    return out
