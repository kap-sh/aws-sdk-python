"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationEvaluatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.recommendation_evaluator_reference

RecommendationEvaluatorList: TypeAlias = list[
    "capo_bedrock_agentcore.types.recommendation_evaluator_reference.RecommendationEvaluatorReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationEvaluatorList) -> list:
    import capo_bedrock_agentcore.types.recommendation_evaluator_reference

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.recommendation_evaluator_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationEvaluatorList:
    import capo_bedrock_agentcore.types.recommendation_evaluator_reference

    out: RecommendationEvaluatorList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore.types.recommendation_evaluator_reference.deserialize_json(
                item
            )
        )
    return out
