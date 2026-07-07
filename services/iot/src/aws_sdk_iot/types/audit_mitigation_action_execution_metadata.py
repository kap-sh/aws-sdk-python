"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionExecutionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_mitigation_actions_execution_status
    import aws_sdk_iot.types.error_code
    import aws_sdk_iot.types.error_message
    import aws_sdk_iot.types.finding_id
    import aws_sdk_iot.types.mitigation_action_id
    import aws_sdk_iot.types.mitigation_action_name
    import aws_sdk_iot.types.mitigation_actions_task_id
    import aws_sdk_iot.types.timestamp


class AuditMitigationActionExecutionMetadata(TypedDict, closed=True):
    task_id: NotRequired[
        "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    ]
    """<p>The unique identifier for the task that applies the mitigation action.</p>"""
    finding_id: NotRequired["aws_sdk_iot.types.finding_id.FindingId"]
    """<p>The unique identifier for the findings to which the task and associated mitigation action are applied.</p>"""
    action_name: NotRequired[
        "aws_sdk_iot.types.mitigation_action_name.MitigationActionName"
    ]
    """<p>The friendly name of the mitigation action being applied by the task.</p>"""
    action_id: NotRequired["aws_sdk_iot.types.mitigation_action_id.MitigationActionId"]
    """<p>The unique identifier for the mitigation action being applied by the task.</p>"""
    status: NotRequired[
        "aws_sdk_iot.types.audit_mitigation_actions_execution_status.AuditMitigationActionsExecutionStatus"
    ]
    """<p>The current status of the task being executed.</p>"""
    start_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The date and time when the task was started.</p>"""
    end_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The date and time when the task was completed or canceled. Blank if the task is still running.</p>"""
    error_code: NotRequired["aws_sdk_iot.types.error_code.ErrorCode"]
    """<p>If an error occurred, the code that indicates which type of error occurred.</p>"""
    message: NotRequired["aws_sdk_iot.types.error_message.ErrorMessage"]
    """<p>If an error occurred, a message that describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditMitigationActionExecutionMetadata) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    if "status" in value:
        import aws_sdk_iot.types.audit_mitigation_actions_execution_status

        out["status"] = (
            aws_sdk_iot.types.audit_mitigation_actions_execution_status.serialize_json(
                value["status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_iot.types.timestamp

        out["startTime"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_iot.types.timestamp

        out["endTime"] = aws_sdk_iot.types.timestamp.serialize_json(value["end_time"])
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AuditMitigationActionExecutionMetadata:
    out: AuditMitigationActionExecutionMetadata = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "findingId" in data:
        out["finding_id"] = data["findingId"]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    if "status" in data:
        import aws_sdk_iot.types.audit_mitigation_actions_execution_status

        out["status"] = (
            aws_sdk_iot.types.audit_mitigation_actions_execution_status.deserialize_json(
                data["status"]
            )
        )
    if "startTime" in data:
        import aws_sdk_iot.types.timestamp

        out["start_time"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_iot.types.timestamp

        out["end_time"] = aws_sdk_iot.types.timestamp.deserialize_json(data["endTime"])
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "message" in data:
        out["message"] = data["message"]
    return out
