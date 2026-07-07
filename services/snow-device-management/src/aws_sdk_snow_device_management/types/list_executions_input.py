"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.execution_state
    import aws_sdk_snow_device_management.types.max_results
    import aws_sdk_snow_device_management.types.next_token
    import aws_sdk_snow_device_management.types.task_id


class ListExecutionsInput(TypedDict, closed=True):
    task_id: "aws_sdk_snow_device_management.types.task_id.TaskId"
    """<p>The ID of the task.</p>"""
    state: NotRequired[
        "aws_sdk_snow_device_management.types.execution_state.ExecutionState"
    ]
    """<p>A structure used to filter the tasks by their current state.</p>"""
    max_results: NotRequired[
        "aws_sdk_snow_device_management.types.max_results.MaxResults"
    ]
    """<p>The maximum number of tasks to list per page.</p>"""
    next_token: NotRequired["aws_sdk_snow_device_management.types.next_token.NextToken"]
    """<p>A pagination token to continue to the next page of tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExecutionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExecutionsInput:
    out: ListExecutionsInput = {}  # type: ignore[typeddict-item]
    return out
