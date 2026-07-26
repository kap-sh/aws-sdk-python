"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowExportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.workflow_export

WorkflowExportList: TypeAlias = list["capo_omics.types.workflow_export.WorkflowExport"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowExportList) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkflowExportList:
    return list(data)
