"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataCellsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.data_cells_filter

DataCellsFilterList: TypeAlias = list[
    "aws_sdk_lakeformation.types.data_cells_filter.DataCellsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataCellsFilterList) -> list:
    import aws_sdk_lakeformation.types.data_cells_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.data_cells_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataCellsFilterList:
    import aws_sdk_lakeformation.types.data_cells_filter

    out: DataCellsFilterList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.data_cells_filter.deserialize_json(item))
    return out
