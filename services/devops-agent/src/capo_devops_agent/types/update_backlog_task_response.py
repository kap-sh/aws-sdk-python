"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateBacklogTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.task


class UpdateBacklogTaskResponse(TypedDict, closed=True):
    task: "capo_devops_agent.types.task.Task"
    """<p>The updated task object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBacklogTaskResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.task

    out["task"] = capo_devops_agent.types.task.serialize_json(value["task"])
    return out


def deserialize_json(data: dict) -> UpdateBacklogTaskResponse:
    out: UpdateBacklogTaskResponse = {}  # type: ignore[typeddict-item]
    if "task" in data:
        import capo_devops_agent.types.task

        out["task"] = capo_devops_agent.types.task.deserialize_json(data["task"])
    else:
        raise DeserializationError("UpdateBacklogTaskResponse.task required")
    return out
