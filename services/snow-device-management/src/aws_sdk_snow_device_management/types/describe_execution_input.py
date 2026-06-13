"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.managed_device_id
    import aws_sdk_snow_device_management.types.task_id


class DescribeExecutionInput(TypedDict):
    task_id: "aws_sdk_snow_device_management.types.task_id.TaskId"
    """<p>The ID of the task that the action is describing.</p>"""
    managed_device_id: (
        "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId"
    )
    """<p>The ID of the managed device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeExecutionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeExecutionInput:
    out: DescribeExecutionInput = {}  # type: ignore[typeddict-item]
    return out
