"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.task_type

TaskTypeList: TypeAlias = list["aws_sdk_devops_agent.types.task_type.TaskType"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskTypeList) -> list:
    import aws_sdk_devops_agent.types.task_type

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.task_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskTypeList:
    import aws_sdk_devops_agent.types.task_type

    out: TaskTypeList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.task_type.deserialize_json(item))
    return out
