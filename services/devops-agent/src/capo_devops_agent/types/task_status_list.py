"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.task_status

TaskStatusList: TypeAlias = list["capo_devops_agent.types.task_status.TaskStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskStatusList) -> list:
    import capo_devops_agent.types.task_status

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.task_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskStatusList:
    import capo_devops_agent.types.task_status

    out: TaskStatusList = []
    for item in data:
        out.append(capo_devops_agent.types.task_status.deserialize_json(item))
    return out
