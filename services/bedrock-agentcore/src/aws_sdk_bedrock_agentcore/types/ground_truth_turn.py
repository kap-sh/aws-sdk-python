"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthTurn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluation_content
    import aws_sdk_bedrock_agentcore.types.ground_truth_turn_input


class GroundTruthTurn(TypedDict, closed=True):
    input: NotRequired[
        "aws_sdk_bedrock_agentcore.types.ground_truth_turn_input.GroundTruthTurnInput"
    ]
    """<p>The input for this conversation turn.</p>"""
    expected_response: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_content.EvaluationContent"
    ]
    """<p>The expected response for this conversation turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthTurn) -> dict:
    out: dict = {}
    if "input" in value:
        import aws_sdk_bedrock_agentcore.types.ground_truth_turn_input

        out["input"] = (
            aws_sdk_bedrock_agentcore.types.ground_truth_turn_input.serialize_json(
                value["input"]
            )
        )
    if "expected_response" in value:
        import aws_sdk_bedrock_agentcore.types.evaluation_content

        out["expectedResponse"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_content.serialize_json(
                value["expected_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GroundTruthTurn:
    out: GroundTruthTurn = {}  # type: ignore[typeddict-item]
    if "input" in data:
        import aws_sdk_bedrock_agentcore.types.ground_truth_turn_input

        out["input"] = (
            aws_sdk_bedrock_agentcore.types.ground_truth_turn_input.deserialize_json(
                data["input"]
            )
        )
    if "expectedResponse" in data:
        import aws_sdk_bedrock_agentcore.types.evaluation_content

        out["expected_response"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_content.deserialize_json(
                data["expectedResponse"]
            )
        )
    return out
