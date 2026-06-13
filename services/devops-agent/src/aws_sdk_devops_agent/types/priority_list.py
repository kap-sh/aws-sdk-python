"""Generated from Smithy shape ``com.amazonaws.devopsagent#PriorityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.priority

PriorityList: TypeAlias = list["aws_sdk_devops_agent.types.priority.Priority"]


# --- restJson1 ser/de ---
def serialize_json(value: PriorityList) -> list:
    import aws_sdk_devops_agent.types.priority

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.priority.serialize_json(item))
    return out


def deserialize_json(data: list) -> PriorityList:
    import aws_sdk_devops_agent.types.priority

    out: PriorityList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.priority.deserialize_json(item))
    return out
