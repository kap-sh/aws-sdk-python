"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.task_id


class DescribeTaskInput(TypedDict, closed=True):
    task_id: "aws_sdk_snow_device_management.types.task_id.TaskId"
    """<p>The ID of the task to be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTaskInput:
    out: DescribeTaskInput = {}  # type: ignore[typeddict-item]
    return out
