"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_search_criteria

AgentStatusSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.agent_status_search_criteria.AgentStatusSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusSearchConditionList) -> list:
    import aws_sdk_connect.types.agent_status_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.agent_status_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentStatusSearchConditionList:
    import aws_sdk_connect.types.agent_status_search_criteria

    out: AgentStatusSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.agent_status_search_criteria.deserialize_json(item)
        )
    return out
