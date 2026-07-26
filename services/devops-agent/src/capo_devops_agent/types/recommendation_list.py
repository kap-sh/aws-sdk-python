"""Generated from Smithy shape ``com.amazonaws.devopsagent#RecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.recommendation

RecommendationList: TypeAlias = list[
    "capo_devops_agent.types.recommendation.Recommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationList) -> list:
    import capo_devops_agent.types.recommendation

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationList:
    import capo_devops_agent.types.recommendation

    out: RecommendationList = []
    for item in data:
        out.append(capo_devops_agent.types.recommendation.deserialize_json(item))
    return out
