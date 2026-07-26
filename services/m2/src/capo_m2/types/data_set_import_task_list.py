"""Generated from Smithy shape ``com.amazonaws.m2#DataSetImportTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.data_set_import_task

DataSetImportTaskList: TypeAlias = list[
    "capo_m2.types.data_set_import_task.DataSetImportTask"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportTaskList) -> list:
    import capo_m2.types.data_set_import_task

    out: list = []
    for item in value:
        out.append(capo_m2.types.data_set_import_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetImportTaskList:
    import capo_m2.types.data_set_import_task

    out: DataSetImportTaskList = []
    for item in data:
        out.append(capo_m2.types.data_set_import_task.deserialize_json(item))
    return out
