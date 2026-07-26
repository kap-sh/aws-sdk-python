"""Generated from Smithy shape ``com.amazonaws.devopsagent#ExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.execution

ExecutionList: TypeAlias = list["capo_devops_agent.types.execution.Execution"]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionList) -> list:
    import capo_devops_agent.types.execution

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExecutionList:
    import capo_devops_agent.types.execution

    out: ExecutionList = []
    for item in data:
        out.append(capo_devops_agent.types.execution.deserialize_json(item))
    return out
