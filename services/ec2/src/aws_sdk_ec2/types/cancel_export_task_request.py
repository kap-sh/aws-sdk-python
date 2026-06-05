"""Generated from Smithy shape ``com.amazonaws.ec2#CancelExportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_vm_task_id


class CancelExportTaskRequest(TypedDict):
    export_task_id: NotRequired["aws_sdk_ec2.types.export_vm_task_id.ExportVmTaskId"]
    """<p>The ID of the export task. This is the ID returned by the <code>CreateInstanceExportTask</code> and <code>ExportImage</code> operations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelExportTaskRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "export_task_id" in value:
        pairs.append((f"{prefix}.ExportTaskId", str(value["export_task_id"])))


def deserialize_ec2_query(el: Element) -> CancelExportTaskRequest:
    out: CancelExportTaskRequest = {}  # type: ignore[typeddict-item]
    child_export_task_id = el.find("ExportTaskId")
    if child_export_task_id is not None:
        out["export_task_id"] = str(child_export_task_id.text or "")
    return out
