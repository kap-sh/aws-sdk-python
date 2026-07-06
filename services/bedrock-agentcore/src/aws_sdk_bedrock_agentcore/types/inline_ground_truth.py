"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InlineGroundTruth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluation_content_list
    import aws_sdk_bedrock_agentcore.types.evaluation_expected_trajectory
    import aws_sdk_bedrock_agentcore.types.ground_truth_turn_list


class InlineGroundTruth(TypedDict, closed=True):
    assertions: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_content_list.EvaluationContentList"
    ]
    """<p>Assertions for evaluation, reuses common model EvaluationContentList.</p>"""
    expected_trajectory: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_expected_trajectory.EvaluationExpectedTrajectory"
    ]
    """<p>The expected tool call sequence for trajectory evaluation.</p>"""
    turns: NotRequired[
        "aws_sdk_bedrock_agentcore.types.ground_truth_turn_list.GroundTruthTurnList"
    ]
    """<p>A list of per-turn ground truth data, each containing an input prompt and expected response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineGroundTruth) -> dict:
    out: dict = {}
    if "assertions" in value:
        import aws_sdk_bedrock_agentcore.types.evaluation_content_list

        out["assertions"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_content_list.serialize_json(
                value["assertions"]
            )
        )
    if "expected_trajectory" in value:
        import aws_sdk_bedrock_agentcore.types.evaluation_expected_trajectory

        out["expectedTrajectory"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_expected_trajectory.serialize_json(
                value["expected_trajectory"]
            )
        )
    if "turns" in value:
        import aws_sdk_bedrock_agentcore.types.ground_truth_turn_list

        out["turns"] = (
            aws_sdk_bedrock_agentcore.types.ground_truth_turn_list.serialize_json(
                value["turns"]
            )
        )
    return out


def deserialize_json(data: dict) -> InlineGroundTruth:
    out: InlineGroundTruth = {}  # type: ignore[typeddict-item]
    if "assertions" in data:
        import aws_sdk_bedrock_agentcore.types.evaluation_content_list

        out["assertions"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_content_list.deserialize_json(
                data["assertions"]
            )
        )
    if "expectedTrajectory" in data:
        import aws_sdk_bedrock_agentcore.types.evaluation_expected_trajectory

        out["expected_trajectory"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_expected_trajectory.deserialize_json(
                data["expectedTrajectory"]
            )
        )
    if "turns" in data:
        import aws_sdk_bedrock_agentcore.types.ground_truth_turn_list

        out["turns"] = (
            aws_sdk_bedrock_agentcore.types.ground_truth_turn_list.deserialize_json(
                data["turns"]
            )
        )
    return out
