"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionTaskInvocationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_execution_id
    import aws_sdk_ssm.types.maintenance_window_execution_task_id
    import aws_sdk_ssm.types.maintenance_window_execution_task_invocation_id


class GetMaintenanceWindowExecutionTaskInvocationRequest(TypedDict):
    window_execution_id: (
        "aws_sdk_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    )
    """<p>The ID of the maintenance window execution for which the task is a part.</p>"""
    task_id: "aws_sdk_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    """<p>The ID of the specific task in the maintenance window task that should be retrieved. </p>"""
    invocation_id: "aws_sdk_ssm.types.maintenance_window_execution_task_invocation_id.MaintenanceWindowExecutionTaskInvocationId"
    """<p>The invocation ID to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetMaintenanceWindowExecutionTaskInvocationRequest,
) -> dict:
    out: dict = {}
    out["WindowExecutionId"] = value["window_execution_id"]
    out["TaskId"] = value["task_id"]
    out["InvocationId"] = value["invocation_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetMaintenanceWindowExecutionTaskInvocationRequest:
    out: GetMaintenanceWindowExecutionTaskInvocationRequest = {}  # type: ignore[typeddict-item]
    if "WindowExecutionId" in data:
        out["window_execution_id"] = data["WindowExecutionId"]
    else:
        raise DeserializationError(
            "GetMaintenanceWindowExecutionTaskInvocationRequest.window_execution_id required"
        )
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    else:
        raise DeserializationError(
            "GetMaintenanceWindowExecutionTaskInvocationRequest.task_id required"
        )
    if "InvocationId" in data:
        out["invocation_id"] = data["InvocationId"]
    else:
        raise DeserializationError(
            "GetMaintenanceWindowExecutionTaskInvocationRequest.invocation_id required"
        )
    return out
