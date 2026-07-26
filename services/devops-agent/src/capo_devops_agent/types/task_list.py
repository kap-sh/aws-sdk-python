"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.task

TaskList: TypeAlias = list["capo_devops_agent.types.task.Task"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskList) -> list:
    import capo_devops_agent.types.task

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.task.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskList:
    import capo_devops_agent.types.task

    out: TaskList = []
    for item in data:
        out.append(capo_devops_agent.types.task.deserialize_json(item))
    return out
