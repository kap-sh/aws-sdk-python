"""Generated from Smithy shape ``com.amazonaws.m2#DataSetExportTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.data_set_export_task

DataSetExportTaskList: TypeAlias = list[
    "aws_sdk_m2.types.data_set_export_task.DataSetExportTask"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetExportTaskList) -> list:
    import aws_sdk_m2.types.data_set_export_task

    out: list = []
    for item in value:
        out.append(aws_sdk_m2.types.data_set_export_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetExportTaskList:
    import aws_sdk_m2.types.data_set_export_task

    out: DataSetExportTaskList = []
    for item in data:
        out.append(aws_sdk_m2.types.data_set_export_task.deserialize_json(item))
    return out
