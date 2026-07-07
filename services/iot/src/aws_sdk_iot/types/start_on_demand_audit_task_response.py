"""Generated from Smithy shape ``com.amazonaws.iot#StartOnDemandAuditTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_task_id


class StartOnDemandAuditTaskResponse(TypedDict, closed=True):
    task_id: NotRequired["aws_sdk_iot.types.audit_task_id.AuditTaskId"]
    """<p>The ID of the on-demand audit you started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOnDemandAuditTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> StartOnDemandAuditTaskResponse:
    out: StartOnDemandAuditTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    return out
