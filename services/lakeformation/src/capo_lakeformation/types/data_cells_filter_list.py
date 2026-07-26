"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataCellsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.data_cells_filter

DataCellsFilterList: TypeAlias = list[
    "capo_lakeformation.types.data_cells_filter.DataCellsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataCellsFilterList) -> list:
    import capo_lakeformation.types.data_cells_filter

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.data_cells_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataCellsFilterList:
    import capo_lakeformation.types.data_cells_filter

    out: DataCellsFilterList = []
    for item in data:
        out.append(capo_lakeformation.types.data_cells_filter.deserialize_json(item))
    return out
