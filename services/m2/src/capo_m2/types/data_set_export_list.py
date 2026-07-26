"""Generated from Smithy shape ``com.amazonaws.m2#DataSetExportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.data_set_export_item

DataSetExportList: TypeAlias = list[
    "capo_m2.types.data_set_export_item.DataSetExportItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetExportList) -> list:
    import capo_m2.types.data_set_export_item

    out: list = []
    for item in value:
        out.append(capo_m2.types.data_set_export_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetExportList:
    import capo_m2.types.data_set_export_item

    out: DataSetExportList = []
    for item in data:
        out.append(capo_m2.types.data_set_export_item.deserialize_json(item))
    return out
