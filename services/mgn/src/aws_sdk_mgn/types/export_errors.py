"""Generated from Smithy shape ``com.amazonaws.mgn#ExportErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.export_task_error

ExportErrors: TypeAlias = list["aws_sdk_mgn.types.export_task_error.ExportTaskError"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportErrors) -> list:
    import aws_sdk_mgn.types.export_task_error

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.export_task_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportErrors:
    import aws_sdk_mgn.types.export_task_error

    out: ExportErrors = []
    for item in data:
        out.append(aws_sdk_mgn.types.export_task_error.deserialize_json(item))
    return out
