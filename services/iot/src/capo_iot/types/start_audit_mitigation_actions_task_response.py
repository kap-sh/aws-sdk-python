"""Generated from Smithy shape ``com.amazonaws.iot#StartAuditMitigationActionsTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.mitigation_actions_task_id


class StartAuditMitigationActionsTaskResponse(TypedDict, closed=True):
    task_id: NotRequired[
        "capo_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    ]
    """<p>The unique identifier for the audit mitigation task. This matches the <code>taskId</code> that you specified in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAuditMitigationActionsTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> StartAuditMitigationActionsTaskResponse:
    out: StartAuditMitigationActionsTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    return out
