"""Generated from Smithy shape ``com.amazonaws.connect#AiAgentSearchCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.ai_agent_search_criteria

AiAgentSearchCriteriaList: TypeAlias = list[
    "aws_sdk_connect.types.ai_agent_search_criteria.AiAgentSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: AiAgentSearchCriteriaList) -> list:
    import aws_sdk_connect.types.ai_agent_search_criteria

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.ai_agent_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> AiAgentSearchCriteriaList:
    import aws_sdk_connect.types.ai_agent_search_criteria

    out: AiAgentSearchCriteriaList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.ai_agent_search_criteria.deserialize_json(item)
        )
    return out
