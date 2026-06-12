"""Generated from Smithy shape ``com.amazonaws.iot#GetCommandExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_arn
    import aws_sdk_iot.types.command_execution_id
    import aws_sdk_iot.types.command_execution_parameter_map
    import aws_sdk_iot.types.command_execution_result_map
    import aws_sdk_iot.types.command_execution_status
    import aws_sdk_iot.types.command_execution_timeout_in_seconds
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.status_reason
    import aws_sdk_iot.types.target_arn


class GetCommandExecutionResponse(TypedDict):
    execution_id: NotRequired[
        "aws_sdk_iot.types.command_execution_id.CommandExecutionId"
    ]
    """<p>The unique identifier of the command execution.</p>"""
    command_arn: NotRequired["aws_sdk_iot.types.command_arn.CommandArn"]
    """<p>The Amazon Resource Number (ARN) of the command. For example, <code></code>arn:aws:iot:<region>:<accountid>:command/<commandId></p>"""
    target_arn: NotRequired["aws_sdk_iot.types.target_arn.TargetArn"]
    """<p>The Amazon Resource Number (ARN) of the device on which the command execution is being performed.</p>"""
    status: NotRequired[
        "aws_sdk_iot.types.command_execution_status.CommandExecutionStatus"
    ]
    """<p>The status of the command execution. After your devices receive the command and start performing the operations specified in the command, it can use the <code>UpdateCommandExecution</code> MQTT API to update the status information.</p>"""
    status_reason: NotRequired["aws_sdk_iot.types.status_reason.StatusReason"]
    """<p>Your devices can use this parameter to provide additional context about the status of a command execution using a reason code and description.</p>"""
    result: NotRequired[
        "aws_sdk_iot.types.command_execution_result_map.CommandExecutionResultMap"
    ]
    """<p>The result value for the current state of the command execution. The status provides information about the progress of the command execution. The device can use the result field to share additional details about the execution such as a return value of a remote function call.</p> <note> <p>If you use the <code>AWS-IoT-FleetWise</code> namespace, then this field is not applicable in the API response.</p> </note>"""
    parameters: NotRequired[
        "aws_sdk_iot.types.command_execution_parameter_map.CommandExecutionParameterMap"
    ]
    """<p>The list of parameters that the <code>StartCommandExecution</code> API used when performing the command on the device.</p>"""
    execution_timeout_seconds: NotRequired[
        "aws_sdk_iot.types.command_execution_timeout_in_seconds.CommandExecutionTimeoutInSeconds"
    ]
    """<p>Specifies the amount of time in seconds that the device can take to finish a command execution. A timer starts when the command execution is created. If the command execution status is not set to another terminal state before the timer expires, it will automatically update to <code>TIMED_OUT</code>.</p>"""
    created_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The timestamp, when the command execution was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The timestamp, when the command execution was last updated.</p>"""
    started_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The timestamp, when the command execution was started.</p>"""
    completed_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The timestamp, when the command execution was completed.</p>"""
    time_to_live: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The time to live (TTL) parameter that indicates the duration for which executions will be retained in your account. The default value is six months.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCommandExecutionResponse) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "command_arn" in value:
        out["commandArn"] = value["command_arn"]
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "status" in value:
        import aws_sdk_iot.types.command_execution_status

        out["status"] = aws_sdk_iot.types.command_execution_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        import aws_sdk_iot.types.status_reason

        out["statusReason"] = aws_sdk_iot.types.status_reason.serialize_json(
            value["status_reason"]
        )
    if "result" in value:
        import aws_sdk_iot.types.command_execution_result_map

        out["result"] = aws_sdk_iot.types.command_execution_result_map.serialize_json(
            value["result"]
        )
    if "parameters" in value:
        import aws_sdk_iot.types.command_execution_parameter_map

        out["parameters"] = (
            aws_sdk_iot.types.command_execution_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    if "execution_timeout_seconds" in value:
        out["executionTimeoutSeconds"] = value["execution_timeout_seconds"]
    if "created_at" in value:
        import aws_sdk_iot.types.date_type

        out["createdAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_iot.types.date_type

        out["lastUpdatedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    if "started_at" in value:
        import aws_sdk_iot.types.date_type

        out["startedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["started_at"]
        )
    if "completed_at" in value:
        import aws_sdk_iot.types.date_type

        out["completedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["completed_at"]
        )
    if "time_to_live" in value:
        import aws_sdk_iot.types.date_type

        out["timeToLive"] = aws_sdk_iot.types.date_type.serialize_json(
            value["time_to_live"]
        )
    return out


def deserialize_json(data: dict) -> GetCommandExecutionResponse:
    out: GetCommandExecutionResponse = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    if "commandArn" in data:
        out["command_arn"] = data["commandArn"]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    if "status" in data:
        import aws_sdk_iot.types.command_execution_status

        out["status"] = aws_sdk_iot.types.command_execution_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        import aws_sdk_iot.types.status_reason

        out["status_reason"] = aws_sdk_iot.types.status_reason.deserialize_json(
            data["statusReason"]
        )
    if "result" in data:
        import aws_sdk_iot.types.command_execution_result_map

        out["result"] = aws_sdk_iot.types.command_execution_result_map.deserialize_json(
            data["result"]
        )
    if "parameters" in data:
        import aws_sdk_iot.types.command_execution_parameter_map

        out["parameters"] = (
            aws_sdk_iot.types.command_execution_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    if "executionTimeoutSeconds" in data:
        out["execution_timeout_seconds"] = data["executionTimeoutSeconds"]
    if "createdAt" in data:
        import aws_sdk_iot.types.date_type

        out["created_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_iot.types.date_type

        out["last_updated_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "startedAt" in data:
        import aws_sdk_iot.types.date_type

        out["started_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["startedAt"]
        )
    if "completedAt" in data:
        import aws_sdk_iot.types.date_type

        out["completed_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["completedAt"]
        )
    if "timeToLive" in data:
        import aws_sdk_iot.types.date_type

        out["time_to_live"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["timeToLive"]
        )
    return out
