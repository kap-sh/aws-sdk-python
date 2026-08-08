"""Generated from Smithy shape ``com.amazonaws.ec2#CancelExportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.export_vm_task_id


class CancelExportTaskRequest(TypedDict, closed=True):
    export_task_id: NotRequired["capo_ec2.types.export_vm_task_id.ExportVmTaskId"]
    """<p>The ID of the export task. This is the ID returned by the <code>CreateInstanceExportTask</code> and <code>ExportImage</code> operations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelExportTaskRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "export_task_id" in value:
        pairs.append((f"{key_prefix}ExportTaskId", str(value["export_task_id"])))


def deserialize_ec2_query(el: Element) -> CancelExportTaskRequest:
    out: CancelExportTaskRequest = {}  # type: ignore[typeddict-item]
    child_export_task_id = el.find("exportTaskId")
    if child_export_task_id is not None:
        out["export_task_id"] = str(child_export_task_id.text or "")
    return out
