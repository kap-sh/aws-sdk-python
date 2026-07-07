"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListBacklogTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.task_list


class ListBacklogTasksResponse(TypedDict, closed=True):
    tasks: "aws_sdk_devops_agent.types.task_list.TaskList"
    """<p>List of backlog tasks</p>"""
    next_token: NotRequired["str"]
    """<p>Token for retrieving the next page of results, if more results are available</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBacklogTasksResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.task_list

    out["tasks"] = aws_sdk_devops_agent.types.task_list.serialize_json(value["tasks"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBacklogTasksResponse:
    out: ListBacklogTasksResponse = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import aws_sdk_devops_agent.types.task_list

        out["tasks"] = aws_sdk_devops_agent.types.task_list.deserialize_json(
            data["tasks"]
        )
    else:
        raise DeserializationError("ListBacklogTasksResponse.tasks required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
