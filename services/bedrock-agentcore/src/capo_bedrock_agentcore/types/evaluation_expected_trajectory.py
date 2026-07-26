"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationExpectedTrajectory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluation_tool_names


class EvaluationExpectedTrajectory(TypedDict, closed=True):
    tool_names: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_tool_names.EvaluationToolNames"
    ]
    """<p> The list of tool names representing the expected tool call sequence. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationExpectedTrajectory) -> dict:
    out: dict = {}
    if "tool_names" in value:
        import capo_bedrock_agentcore.types.evaluation_tool_names

        out["toolNames"] = (
            capo_bedrock_agentcore.types.evaluation_tool_names.serialize_json(
                value["tool_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationExpectedTrajectory:
    out: EvaluationExpectedTrajectory = {}  # type: ignore[typeddict-item]
    if "toolNames" in data:
        import capo_bedrock_agentcore.types.evaluation_tool_names

        out["tool_names"] = (
            capo_bedrock_agentcore.types.evaluation_tool_names.deserialize_json(
                data["toolNames"]
            )
        )
    return out
