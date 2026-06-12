"""Generated from Smithy shape ``com.amazonaws.m2#DataSetImportTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.data_set_import_task

DataSetImportTaskList: TypeAlias = list[
    "aws_sdk_m2.types.data_set_import_task.DataSetImportTask"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportTaskList) -> list:
    import aws_sdk_m2.types.data_set_import_task

    out: list = []
    for item in value:
        out.append(aws_sdk_m2.types.data_set_import_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetImportTaskList:
    import aws_sdk_m2.types.data_set_import_task

    out: DataSetImportTaskList = []
    for item in data:
        out.append(aws_sdk_m2.types.data_set_import_task.deserialize_json(item))
    return out
