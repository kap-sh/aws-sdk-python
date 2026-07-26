"""Generated from Smithy shape ``com.amazonaws.devopsagent#PriorityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.priority

PriorityList: TypeAlias = list["capo_devops_agent.types.priority.Priority"]


# --- restJson1 ser/de ---
def serialize_json(value: PriorityList) -> list:
    import capo_devops_agent.types.priority

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.priority.serialize_json(item))
    return out


def deserialize_json(data: list) -> PriorityList:
    import capo_devops_agent.types.priority

    out: PriorityList = []
    for item in data:
        out.append(capo_devops_agent.types.priority.deserialize_json(item))
    return out
