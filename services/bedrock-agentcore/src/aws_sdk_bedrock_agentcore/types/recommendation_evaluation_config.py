"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationEvaluationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.recommendation_evaluator_list


class RecommendationEvaluationConfig(TypedDict, closed=True):
    evaluators: "aws_sdk_bedrock_agentcore.types.recommendation_evaluator_list.RecommendationEvaluatorList"
    """<p>The list of evaluators to use for assessing recommendation quality.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationEvaluationConfig) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.recommendation_evaluator_list

    out["evaluators"] = (
        aws_sdk_bedrock_agentcore.types.recommendation_evaluator_list.serialize_json(
            value["evaluators"]
        )
    )
    return out


def deserialize_json(data: dict) -> RecommendationEvaluationConfig:
    out: RecommendationEvaluationConfig = {}  # type: ignore[typeddict-item]
    if "evaluators" in data:
        import aws_sdk_bedrock_agentcore.types.recommendation_evaluator_list

        out["evaluators"] = (
            aws_sdk_bedrock_agentcore.types.recommendation_evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    else:
        raise DeserializationError("RecommendationEvaluationConfig.evaluators required")
    return out
