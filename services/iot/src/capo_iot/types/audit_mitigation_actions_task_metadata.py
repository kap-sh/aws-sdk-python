"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionsTaskMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_mitigation_actions_task_status
    import capo_iot.types.mitigation_actions_task_id
    import capo_iot.types.timestamp


class AuditMitigationActionsTaskMetadata(TypedDict, closed=True):
    task_id: NotRequired[
        "capo_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    ]
    """<p>The unique identifier for the task.</p>"""
    start_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The time at which the audit mitigation actions task was started.</p>"""
    task_status: NotRequired[
        "capo_iot.types.audit_mitigation_actions_task_status.AuditMitigationActionsTaskStatus"
    ]
    """<p>The current state of the audit mitigation actions task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditMitigationActionsTaskMetadata) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "start_time" in value:
        import capo_iot.types.timestamp

        out["startTime"] = capo_iot.types.timestamp.serialize_json(value["start_time"])
    if "task_status" in value:
        import capo_iot.types.audit_mitigation_actions_task_status

        out["taskStatus"] = (
            capo_iot.types.audit_mitigation_actions_task_status.serialize_json(
                value["task_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuditMitigationActionsTaskMetadata:
    out: AuditMitigationActionsTaskMetadata = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "startTime" in data:
        import capo_iot.types.timestamp

        out["start_time"] = capo_iot.types.timestamp.deserialize_json(data["startTime"])
    if "taskStatus" in data:
        import capo_iot.types.audit_mitigation_actions_task_status

        out["task_status"] = (
            capo_iot.types.audit_mitigation_actions_task_status.deserialize_json(
                data["taskStatus"]
            )
        )
    return out
