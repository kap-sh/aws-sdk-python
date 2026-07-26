"""Generated from Smithy shape ``com.amazonaws.databrew#ColumnSelectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.column_selector

ColumnSelectorList: TypeAlias = list[
    "capo_databrew.types.column_selector.ColumnSelector"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSelectorList) -> list:
    import capo_databrew.types.column_selector

    out: list = []
    for item in value:
        out.append(capo_databrew.types.column_selector.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnSelectorList:
    import capo_databrew.types.column_selector

    out: ColumnSelectorList = []
    for item in data:
        out.append(capo_databrew.types.column_selector.deserialize_json(item))
    return out
