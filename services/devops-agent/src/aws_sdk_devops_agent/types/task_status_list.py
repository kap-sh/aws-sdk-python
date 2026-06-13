"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.task_status

TaskStatusList: TypeAlias = list["aws_sdk_devops_agent.types.task_status.TaskStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskStatusList) -> list:
    import aws_sdk_devops_agent.types.task_status

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.task_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskStatusList:
    import aws_sdk_devops_agent.types.task_status

    out: TaskStatusList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.task_status.deserialize_json(item))
    return out
