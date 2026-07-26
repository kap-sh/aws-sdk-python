"""Generated from Smithy shape ``com.amazonaws.datazone#RowFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.row_filter

RowFilterList: TypeAlias = list["capo_datazone.types.row_filter.RowFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: RowFilterList) -> list:
    import capo_datazone.types.row_filter

    out: list = []
    for item in value:
        out.append(capo_datazone.types.row_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> RowFilterList:
    import capo_datazone.types.row_filter

    out: RowFilterList = []
    for item in data:
        out.append(capo_datazone.types.row_filter.deserialize_json(item))
    return out
