"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionTaskInvocationIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.maintenance_window_execution_id
    import aws_sdk_ssm.types.maintenance_window_execution_status
    import aws_sdk_ssm.types.maintenance_window_execution_status_details
    import aws_sdk_ssm.types.maintenance_window_execution_task_execution_id
    import aws_sdk_ssm.types.maintenance_window_execution_task_id
    import aws_sdk_ssm.types.maintenance_window_execution_task_invocation_id
    import aws_sdk_ssm.types.maintenance_window_execution_task_invocation_parameters
    import aws_sdk_ssm.types.maintenance_window_task_target_id
    import aws_sdk_ssm.types.maintenance_window_task_type
    import aws_sdk_ssm.types.owner_information


class MaintenanceWindowExecutionTaskInvocationIdentity(TypedDict, closed=True):
    window_execution_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    ]
    """<p>The ID of the maintenance window execution that ran the task.</p>"""
    task_execution_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    ]
    """<p>The ID of the specific task execution in the maintenance window execution.</p>"""
    invocation_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_task_invocation_id.MaintenanceWindowExecutionTaskInvocationId"
    ]
    """<p>The ID of the task invocation.</p>"""
    execution_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_task_execution_id.MaintenanceWindowExecutionTaskExecutionId"
    ]
    """<p>The ID of the action performed in the service that actually handled the task invocation. If the task type is <code>RUN_COMMAND</code>, this value is the command ID.</p>"""
    task_type: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_type.MaintenanceWindowTaskType"
    ]
    """<p>The task type.</p>"""
    parameters: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_task_invocation_parameters.MaintenanceWindowExecutionTaskInvocationParameters"
    ]
    """<p>The parameters that were provided for the invocation when it was run.</p>"""
    status: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_status.MaintenanceWindowExecutionStatus"
    ]
    """<p>The status of the task invocation.</p>"""
    status_details: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_status_details.MaintenanceWindowExecutionStatusDetails"
    ]
    """<p>The details explaining the status of the task invocation. Not available for all status values. </p>"""
    start_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time the invocation started.</p>"""
    end_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time the invocation finished.</p>"""
    owner_information: NotRequired[
        "aws_sdk_ssm.types.owner_information.OwnerInformation"
    ]
    """<p>User-provided value that was specified when the target was registered with the maintenance window. This was also included in any Amazon CloudWatch Events events raised during the task invocation.</p>"""
    window_target_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_target_id.MaintenanceWindowTaskTargetId"
    ]
    """<p>The ID of the target definition in this maintenance window the invocation was performed for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: MaintenanceWindowExecutionTaskInvocationIdentity,
) -> dict:
    out: dict = {}
    if "window_execution_id" in value:
        out["WindowExecutionId"] = value["window_execution_id"]
    if "task_execution_id" in value:
        out["TaskExecutionId"] = value["task_execution_id"]
    if "invocation_id" in value:
        out["InvocationId"] = value["invocation_id"]
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "task_type" in value:
        import aws_sdk_ssm.types.maintenance_window_task_type

        out["TaskType"] = (
            aws_sdk_ssm.types.maintenance_window_task_type.serialize_aws_json_1_1(
                value["task_type"]
            )
        )
    if "parameters" in value:
        out["Parameters"] = value["parameters"]
    if "status" in value:
        import aws_sdk_ssm.types.maintenance_window_execution_status

        out["Status"] = (
            aws_sdk_ssm.types.maintenance_window_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "start_time" in value:
        import aws_sdk_ssm.types.date_time

        out["StartTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_ssm.types.date_time

        out["EndTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "owner_information" in value:
        out["OwnerInformation"] = value["owner_information"]
    if "window_target_id" in value:
        out["WindowTargetId"] = value["window_target_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> MaintenanceWindowExecutionTaskInvocationIdentity:
    out: MaintenanceWindowExecutionTaskInvocationIdentity = {}  # type: ignore[typeddict-item]
    if "WindowExecutionId" in data:
        out["window_execution_id"] = data["WindowExecutionId"]
    if "TaskExecutionId" in data:
        out["task_execution_id"] = data["TaskExecutionId"]
    if "InvocationId" in data:
        out["invocation_id"] = data["InvocationId"]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    if "TaskType" in data:
        import aws_sdk_ssm.types.maintenance_window_task_type

        out["task_type"] = (
            aws_sdk_ssm.types.maintenance_window_task_type.deserialize_aws_json_1_1(
                data["TaskType"]
            )
        )
    if "Parameters" in data:
        out["parameters"] = data["Parameters"]
    if "Status" in data:
        import aws_sdk_ssm.types.maintenance_window_execution_status

        out["status"] = (
            aws_sdk_ssm.types.maintenance_window_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusDetails" in data:
        out["status_details"] = data["StatusDetails"]
    if "StartTime" in data:
        import aws_sdk_ssm.types.date_time

        out["start_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_ssm.types.date_time

        out["end_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "OwnerInformation" in data:
        out["owner_information"] = data["OwnerInformation"]
    if "WindowTargetId" in data:
        out["window_target_id"] = data["WindowTargetId"]
    return out
