"""Generated from Smithy shape ``com.amazonaws.mgn#ExportsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_mgn.types.export_task

ExportsList: TypeAlias = list["aws_sdk_mgn.types.export_task.ExportTask"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportsList) -> list:
    import aws_sdk_mgn.types.export_task
    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.export_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportsList:
    import aws_sdk_mgn.types.export_task
    out: ExportsList = []
    for item in data:
        out.append(aws_sdk_mgn.types.export_task.deserialize_json(item))
    return out