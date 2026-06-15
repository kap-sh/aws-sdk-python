"""Generated from Smithy shape ``com.amazonaws.iot#AuditTaskMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_task_id
    import aws_sdk_iot.types.audit_task_status
    import aws_sdk_iot.types.audit_task_type


class AuditTaskMetadata(TypedDict):
    task_id: NotRequired["aws_sdk_iot.types.audit_task_id.AuditTaskId"]
    """<p>The ID of this audit.</p>"""
    task_status: NotRequired["aws_sdk_iot.types.audit_task_status.AuditTaskStatus"]
    r"""<p>The status of this audit. One of \"IN_PROGRESS\", \"COMPLETED\", \"FAILED\", or \"CANCELED\".</p>"""
    task_type: NotRequired["aws_sdk_iot.types.audit_task_type.AuditTaskType"]
    r"""<p>The type of this audit. One of \"ON_DEMAND_AUDIT_TASK\" or \"SCHEDULED_AUDIT_TASK\".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditTaskMetadata) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "task_status" in value:
        import aws_sdk_iot.types.audit_task_status

        out["taskStatus"] = aws_sdk_iot.types.audit_task_status.serialize_json(
            value["task_status"]
        )
    if "task_type" in value:
        import aws_sdk_iot.types.audit_task_type

        out["taskType"] = aws_sdk_iot.types.audit_task_type.serialize_json(
            value["task_type"]
        )
    return out


def deserialize_json(data: dict) -> AuditTaskMetadata:
    out: AuditTaskMetadata = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "taskStatus" in data:
        import aws_sdk_iot.types.audit_task_status

        out["task_status"] = aws_sdk_iot.types.audit_task_status.deserialize_json(
            data["taskStatus"]
        )
    if "taskType" in data:
        import aws_sdk_iot.types.audit_task_type

        out["task_type"] = aws_sdk_iot.types.audit_task_type.deserialize_json(
            data["taskType"]
        )
    return out
