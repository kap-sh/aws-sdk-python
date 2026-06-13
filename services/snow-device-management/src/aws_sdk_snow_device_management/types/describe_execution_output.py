"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeExecutionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_snow_device_management.types.execution_id
    import aws_sdk_snow_device_management.types.execution_state
    import aws_sdk_snow_device_management.types.managed_device_id
    import aws_sdk_snow_device_management.types.task_id


class DescribeExecutionOutput(TypedDict):
    task_id: NotRequired["aws_sdk_snow_device_management.types.task_id.TaskId"]
    """<p>The ID of the task being executed on the device.</p>"""
    execution_id: NotRequired[
        "aws_sdk_snow_device_management.types.execution_id.ExecutionId"
    ]
    """<p>The ID of the execution.</p>"""
    managed_device_id: NotRequired[
        "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId"
    ]
    """<p>The ID of the managed device that the task is being executed on.</p>"""
    state: NotRequired[
        "aws_sdk_snow_device_management.types.execution_state.ExecutionState"
    ]
    """<p>The current state of the execution.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>When the execution began.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>When the status of the execution was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeExecutionOutput) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "managed_device_id" in value:
        out["managedDeviceId"] = value["managed_device_id"]
    if "state" in value:
        out["state"] = value["state"]
    if "started_at" in value:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["startedAt"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.serialize_json(
                value["started_at"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeExecutionOutput:
    out: DescribeExecutionOutput = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    if "managedDeviceId" in data:
        out["managed_device_id"] = data["managedDeviceId"]
    if "state" in data:
        out["state"] = data["state"]
    if "startedAt" in data:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["started_at"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["startedAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
