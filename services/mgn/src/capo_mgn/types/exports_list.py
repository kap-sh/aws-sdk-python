"""Generated from Smithy shape ``com.amazonaws.mgn#ExportsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.export_task

ExportsList: TypeAlias = list["capo_mgn.types.export_task.ExportTask"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportsList) -> list:
    import capo_mgn.types.export_task

    out: list = []
    for item in value:
        out.append(capo_mgn.types.export_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportsList:
    import capo_mgn.types.export_task

    out: ExportsList = []
    for item in data:
        out.append(capo_mgn.types.export_task.deserialize_json(item))
    return out
