"""Generated from Smithy shape ``com.amazonaws.datazone#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.filter_clause

FilterList: TypeAlias = list["capo_datazone.types.filter_clause.FilterClause"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    import capo_datazone.types.filter_clause

    out: list = []
    for item in value:
        out.append(capo_datazone.types.filter_clause.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterList:
    import capo_datazone.types.filter_clause

    out: FilterList = []
    for item in data:
        out.append(capo_datazone.types.filter_clause.deserialize_json(item))
    return out
