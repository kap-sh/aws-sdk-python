"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationEvaluatorReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluator_arn


class RecommendationEvaluatorReference(TypedDict, closed=True):
    evaluator_arn: "aws_sdk_bedrock_agentcore.types.evaluator_arn.EvaluatorArn"
    """<p>The Amazon Resource Name (ARN) of the evaluator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationEvaluatorReference) -> dict:
    out: dict = {}
    out["evaluatorArn"] = value["evaluator_arn"]
    return out


def deserialize_json(data: dict) -> RecommendationEvaluatorReference:
    out: RecommendationEvaluatorReference = {}  # type: ignore[typeddict-item]
    if "evaluatorArn" in data:
        out["evaluator_arn"] = data["evaluatorArn"]
    else:
        raise DeserializationError(
            "RecommendationEvaluatorReference.evaluator_arn required"
        )
    return out
