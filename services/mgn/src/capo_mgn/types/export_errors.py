"""Generated from Smithy shape ``com.amazonaws.mgn#ExportErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.export_task_error

ExportErrors: TypeAlias = list["capo_mgn.types.export_task_error.ExportTaskError"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportErrors) -> list:
    import capo_mgn.types.export_task_error

    out: list = []
    for item in value:
        out.append(capo_mgn.types.export_task_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportErrors:
    import capo_mgn.types.export_task_error

    out: ExportErrors = []
    for item in data:
        out.append(capo_mgn.types.export_task_error.deserialize_json(item))
    return out
