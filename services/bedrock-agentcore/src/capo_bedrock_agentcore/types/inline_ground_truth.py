"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InlineGroundTruth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluation_content_list
    import capo_bedrock_agentcore.types.evaluation_expected_trajectory
    import capo_bedrock_agentcore.types.ground_truth_turn_list


class InlineGroundTruth(TypedDict, closed=True):
    assertions: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_content_list.EvaluationContentList"
    ]
    """<p>Assertions for evaluation, reuses common model EvaluationContentList.</p>"""
    expected_trajectory: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_expected_trajectory.EvaluationExpectedTrajectory"
    ]
    """<p>The expected tool call sequence for trajectory evaluation.</p>"""
    turns: NotRequired[
        "capo_bedrock_agentcore.types.ground_truth_turn_list.GroundTruthTurnList"
    ]
    """<p>A list of per-turn ground truth data, each containing an input prompt and expected response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineGroundTruth) -> dict:
    out: dict = {}
    if "assertions" in value:
        import capo_bedrock_agentcore.types.evaluation_content_list

        out["assertions"] = (
            capo_bedrock_agentcore.types.evaluation_content_list.serialize_json(
                value["assertions"]
            )
        )
    if "expected_trajectory" in value:
        import capo_bedrock_agentcore.types.evaluation_expected_trajectory

        out["expectedTrajectory"] = (
            capo_bedrock_agentcore.types.evaluation_expected_trajectory.serialize_json(
                value["expected_trajectory"]
            )
        )
    if "turns" in value:
        import capo_bedrock_agentcore.types.ground_truth_turn_list

        out["turns"] = (
            capo_bedrock_agentcore.types.ground_truth_turn_list.serialize_json(
                value["turns"]
            )
        )
    return out


def deserialize_json(data: dict) -> InlineGroundTruth:
    out: InlineGroundTruth = {}  # type: ignore[typeddict-item]
    if data.get("assertions") is not None:
        import capo_bedrock_agentcore.types.evaluation_content_list

        out["assertions"] = (
            capo_bedrock_agentcore.types.evaluation_content_list.deserialize_json(
                data["assertions"]
            )
        )
    if data.get("expectedTrajectory") is not None:
        import capo_bedrock_agentcore.types.evaluation_expected_trajectory

        out["expected_trajectory"] = (
            capo_bedrock_agentcore.types.evaluation_expected_trajectory.deserialize_json(
                data["expectedTrajectory"]
            )
        )
    if data.get("turns") is not None:
        import capo_bedrock_agentcore.types.ground_truth_turn_list

        out["turns"] = (
            capo_bedrock_agentcore.types.ground_truth_turn_list.deserialize_json(
                data["turns"]
            )
        )
    return out
