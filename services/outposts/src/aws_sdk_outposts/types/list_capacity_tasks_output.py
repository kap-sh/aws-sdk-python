"""Generated from Smithy shape ``com.amazonaws.outposts#ListCapacityTasksOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.capacity_task_list
    import aws_sdk_outposts.types.token


class ListCapacityTasksOutput(TypedDict):
    capacity_tasks: NotRequired[
        "aws_sdk_outposts.types.capacity_task_list.CapacityTaskList"
    ]
    """<p>Lists all the capacity tasks.</p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListCapacityTasksOutput) -> dict:
    out: dict = {}
    if "capacity_tasks" in value:
        import aws_sdk_outposts.types.capacity_task_list

        out["CapacityTasks"] = aws_sdk_outposts.types.capacity_task_list.serialize_json(
            value["capacity_tasks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCapacityTasksOutput:
    out: ListCapacityTasksOutput = {}  # type: ignore[typeddict-item]
    if "CapacityTasks" in data:
        import aws_sdk_outposts.types.capacity_task_list

        out["capacity_tasks"] = (
            aws_sdk_outposts.types.capacity_task_list.deserialize_json(
                data["CapacityTasks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
