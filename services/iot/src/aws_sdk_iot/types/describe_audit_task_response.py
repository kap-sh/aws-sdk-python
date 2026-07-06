"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuditTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_details
    import aws_sdk_iot.types.audit_task_status
    import aws_sdk_iot.types.audit_task_type
    import aws_sdk_iot.types.scheduled_audit_name
    import aws_sdk_iot.types.task_statistics
    import aws_sdk_iot.types.timestamp


class DescribeAuditTaskResponse(TypedDict, closed=True):
    task_status: NotRequired["aws_sdk_iot.types.audit_task_status.AuditTaskStatus"]
    r"""<p>The status of the audit: one of \"IN_PROGRESS\", \"COMPLETED\", \"FAILED\", or \"CANCELED\".</p>"""
    task_type: NotRequired["aws_sdk_iot.types.audit_task_type.AuditTaskType"]
    r"""<p>The type of audit: \"ON_DEMAND_AUDIT_TASK\" or \"SCHEDULED_AUDIT_TASK\".</p>"""
    task_start_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The time the audit started.</p>"""
    task_statistics: NotRequired["aws_sdk_iot.types.task_statistics.TaskStatistics"]
    """<p>Statistical information about the audit.</p>"""
    scheduled_audit_name: NotRequired[
        "aws_sdk_iot.types.scheduled_audit_name.ScheduledAuditName"
    ]
    """<p>The name of the scheduled audit (only if the audit was a scheduled audit).</p>"""
    audit_details: NotRequired["aws_sdk_iot.types.audit_details.AuditDetails"]
    """<p>Detailed information about each check performed during this audit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuditTaskResponse) -> dict:
    out: dict = {}
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
    if "task_start_time" in value:
        import aws_sdk_iot.types.timestamp

        out["taskStartTime"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["task_start_time"]
        )
    if "task_statistics" in value:
        import aws_sdk_iot.types.task_statistics

        out["taskStatistics"] = aws_sdk_iot.types.task_statistics.serialize_json(
            value["task_statistics"]
        )
    if "scheduled_audit_name" in value:
        out["scheduledAuditName"] = value["scheduled_audit_name"]
    if "audit_details" in value:
        import aws_sdk_iot.types.audit_details

        out["auditDetails"] = aws_sdk_iot.types.audit_details.serialize_json(
            value["audit_details"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAuditTaskResponse:
    out: DescribeAuditTaskResponse = {}  # type: ignore[typeddict-item]
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
    if "taskStartTime" in data:
        import aws_sdk_iot.types.timestamp

        out["task_start_time"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["taskStartTime"]
        )
    if "taskStatistics" in data:
        import aws_sdk_iot.types.task_statistics

        out["task_statistics"] = aws_sdk_iot.types.task_statistics.deserialize_json(
            data["taskStatistics"]
        )
    if "scheduledAuditName" in data:
        out["scheduled_audit_name"] = data["scheduledAuditName"]
    if "auditDetails" in data:
        import aws_sdk_iot.types.audit_details

        out["audit_details"] = aws_sdk_iot.types.audit_details.deserialize_json(
            data["auditDetails"]
        )
    return out
