"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListTasksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.max_results
    import aws_sdk_snow_device_management.types.next_token
    import aws_sdk_snow_device_management.types.task_state


class ListTasksInput(TypedDict, closed=True):
    state: NotRequired["aws_sdk_snow_device_management.types.task_state.TaskState"]
    """<p>A structure used to filter the list of tasks.</p>"""
    max_results: NotRequired[
        "aws_sdk_snow_device_management.types.max_results.MaxResults"
    ]
    """<p>The maximum number of tasks per page.</p>"""
    next_token: NotRequired["aws_sdk_snow_device_management.types.next_token.NextToken"]
    """<p>A pagination token to continue to the next page of tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTasksInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTasksInput:
    out: ListTasksInput = {}  # type: ignore[typeddict-item]
    return out
