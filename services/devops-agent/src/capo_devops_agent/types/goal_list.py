"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.goal

GoalList: TypeAlias = list["capo_devops_agent.types.goal.Goal"]


# --- restJson1 ser/de ---
def serialize_json(value: GoalList) -> list:
    import capo_devops_agent.types.goal

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.goal.serialize_json(item))
    return out


def deserialize_json(data: list) -> GoalList:
    import capo_devops_agent.types.goal

    out: GoalList = []
    for item in data:
        out.append(capo_devops_agent.types.goal.deserialize_json(item))
    return out
