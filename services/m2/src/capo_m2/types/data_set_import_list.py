"""Generated from Smithy shape ``com.amazonaws.m2#DataSetImportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.data_set_import_item

DataSetImportList: TypeAlias = list[
    "capo_m2.types.data_set_import_item.DataSetImportItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportList) -> list:
    import capo_m2.types.data_set_import_item

    out: list = []
    for item in value:
        out.append(capo_m2.types.data_set_import_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetImportList:
    import capo_m2.types.data_set_import_item

    out: DataSetImportList = []
    for item in data:
        out.append(capo_m2.types.data_set_import_item.deserialize_json(item))
    return out
