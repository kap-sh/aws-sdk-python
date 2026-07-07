"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.detect_mitigation_action_execution_error_code
    import aws_sdk_iot.types.detect_mitigation_action_execution_status
    import aws_sdk_iot.types.device_defender_thing_name
    import aws_sdk_iot.types.error_message
    import aws_sdk_iot.types.mitigation_action_name
    import aws_sdk_iot.types.mitigation_actions_task_id
    import aws_sdk_iot.types.timestamp
    import aws_sdk_iot.types.violation_id


class DetectMitigationActionExecution(TypedDict, closed=True):
    task_id: NotRequired[
        "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    ]
    """<p> The unique identifier of the task. </p>"""
    violation_id: NotRequired["aws_sdk_iot.types.violation_id.ViolationId"]
    """<p> The unique identifier of the violation. </p>"""
    action_name: NotRequired[
        "aws_sdk_iot.types.mitigation_action_name.MitigationActionName"
    ]
    """<p> The friendly name that uniquely identifies the mitigation action. </p>"""
    thing_name: NotRequired[
        "aws_sdk_iot.types.device_defender_thing_name.DeviceDefenderThingName"
    ]
    """<p> The name of the thing. </p>"""
    execution_start_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The date a mitigation action was started. </p>"""
    execution_end_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The date a mitigation action ended. </p>"""
    status: NotRequired[
        "aws_sdk_iot.types.detect_mitigation_action_execution_status.DetectMitigationActionExecutionStatus"
    ]
    """<p> The status of a mitigation action. </p>"""
    error_code: NotRequired[
        "aws_sdk_iot.types.detect_mitigation_action_execution_error_code.DetectMitigationActionExecutionErrorCode"
    ]
    """<p> The error code of a mitigation action. </p>"""
    message: NotRequired["aws_sdk_iot.types.error_message.ErrorMessage"]
    """<p> The message of a mitigation action. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionExecution) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "violation_id" in value:
        out["violationId"] = value["violation_id"]
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "execution_start_date" in value:
        import aws_sdk_iot.types.timestamp

        out["executionStartDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["execution_start_date"]
        )
    if "execution_end_date" in value:
        import aws_sdk_iot.types.timestamp

        out["executionEndDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["execution_end_date"]
        )
    if "status" in value:
        import aws_sdk_iot.types.detect_mitigation_action_execution_status

        out["status"] = (
            aws_sdk_iot.types.detect_mitigation_action_execution_status.serialize_json(
                value["status"]
            )
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DetectMitigationActionExecution:
    out: DetectMitigationActionExecution = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "violationId" in data:
        out["violation_id"] = data["violationId"]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "executionStartDate" in data:
        import aws_sdk_iot.types.timestamp

        out["execution_start_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["executionStartDate"]
        )
    if "executionEndDate" in data:
        import aws_sdk_iot.types.timestamp

        out["execution_end_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["executionEndDate"]
        )
    if "status" in data:
        import aws_sdk_iot.types.detect_mitigation_action_execution_status

        out["status"] = (
            aws_sdk_iot.types.detect_mitigation_action_execution_status.deserialize_json(
                data["status"]
            )
        )
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "message" in data:
        out["message"] = data["message"]
    return out
