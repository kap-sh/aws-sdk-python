"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthTurn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluation_content
    import capo_bedrock_agentcore.types.ground_truth_turn_input


class GroundTruthTurn(TypedDict, closed=True):
    input: NotRequired[
        "capo_bedrock_agentcore.types.ground_truth_turn_input.GroundTruthTurnInput"
    ]
    """<p>The input for this conversation turn.</p>"""
    expected_response: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_content.EvaluationContent"
    ]
    """<p>The expected response for this conversation turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthTurn) -> dict:
    out: dict = {}
    if "input" in value:
        import capo_bedrock_agentcore.types.ground_truth_turn_input

        out["input"] = (
            capo_bedrock_agentcore.types.ground_truth_turn_input.serialize_json(
                value["input"]
            )
        )
    if "expected_response" in value:
        import capo_bedrock_agentcore.types.evaluation_content

        out["expectedResponse"] = (
            capo_bedrock_agentcore.types.evaluation_content.serialize_json(
                value["expected_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GroundTruthTurn:
    out: GroundTruthTurn = {}  # type: ignore[typeddict-item]
    if data.get("input") is not None:
        import capo_bedrock_agentcore.types.ground_truth_turn_input

        out["input"] = (
            capo_bedrock_agentcore.types.ground_truth_turn_input.deserialize_json(
                data["input"]
            )
        )
    if data.get("expectedResponse") is not None:
        import capo_bedrock_agentcore.types.evaluation_content

        out["expected_response"] = (
            capo_bedrock_agentcore.types.evaluation_content.deserialize_json(
                data["expectedResponse"]
            )
        )
    return out
