"""Generated from Smithy shape ``com.amazonaws.ec2#CancelImportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.import_task_id
    import capo_ec2.types.string


class CancelImportTaskRequest(TypedDict, closed=True):
    cancel_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for canceling the task.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    import_task_id: NotRequired["capo_ec2.types.import_task_id.ImportTaskId"]
    """<p>The ID of the import image or import snapshot task to be canceled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelImportTaskRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cancel_reason" in value:
        pairs.append((f"{key_prefix}CancelReason", str(value["cancel_reason"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "import_task_id" in value:
        pairs.append((f"{key_prefix}ImportTaskId", str(value["import_task_id"])))


def deserialize_ec2_query(el: Element) -> CancelImportTaskRequest:
    out: CancelImportTaskRequest = {}  # type: ignore[typeddict-item]
    child_cancel_reason = el.find("CancelReason")
    if child_cancel_reason is not None:
        out["cancel_reason"] = str(child_cancel_reason.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_import_task_id = el.find("ImportTaskId")
    if child_import_task_id is not None:
        out["import_task_id"] = str(child_import_task_id.text or "")
    return out
