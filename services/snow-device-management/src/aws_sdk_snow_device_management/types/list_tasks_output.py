"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListTasksOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.next_token
    import aws_sdk_snow_device_management.types.task_summary_list


class ListTasksOutput(TypedDict):
    tasks: NotRequired[
        "aws_sdk_snow_device_management.types.task_summary_list.TaskSummaryList"
    ]
    """<p>A list of task structures containing details about each task.</p>"""
    next_token: NotRequired["aws_sdk_snow_device_management.types.next_token.NextToken"]
    """<p>A pagination token to continue to the next page of tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTasksOutput) -> dict:
    out: dict = {}
    if "tasks" in value:
        import aws_sdk_snow_device_management.types.task_summary_list

        out["tasks"] = (
            aws_sdk_snow_device_management.types.task_summary_list.serialize_json(
                value["tasks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTasksOutput:
    out: ListTasksOutput = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import aws_sdk_snow_device_management.types.task_summary_list

        out["tasks"] = (
            aws_sdk_snow_device_management.types.task_summary_list.deserialize_json(
                data["tasks"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
