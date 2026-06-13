"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetBacklogTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.task


class GetBacklogTaskResponse(TypedDict):
    task: "aws_sdk_devops_agent.types.task.Task"
    """<p>The requested task object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBacklogTaskResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.task

    out["task"] = aws_sdk_devops_agent.types.task.serialize_json(value["task"])
    return out


def deserialize_json(data: dict) -> GetBacklogTaskResponse:
    out: GetBacklogTaskResponse = {}  # type: ignore[typeddict-item]
    if "task" in data:
        import aws_sdk_devops_agent.types.task

        out["task"] = aws_sdk_devops_agent.types.task.deserialize_json(data["task"])
    else:
        raise DeserializationError("GetBacklogTaskResponse.task required")
    return out
