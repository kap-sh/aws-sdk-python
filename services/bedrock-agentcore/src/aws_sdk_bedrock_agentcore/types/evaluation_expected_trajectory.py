"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationExpectedTrajectory``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluation_tool_names

class EvaluationExpectedTrajectory(TypedDict):
    tool_names: NotRequired["aws_sdk_bedrock_agentcore.types.evaluation_tool_names.EvaluationToolNames"]
    """<p> The list of tool names representing the expected tool call sequence. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EvaluationExpectedTrajectory) -> dict:
    out: dict = {}
    if "tool_names" in value:
        import aws_sdk_bedrock_agentcore.types.evaluation_tool_names
        out["toolNames"] = aws_sdk_bedrock_agentcore.types.evaluation_tool_names.serialize_json(value["tool_names"])
    return out


def deserialize_json(data: dict) -> EvaluationExpectedTrajectory:
    out: EvaluationExpectedTrajectory = {}  # type: ignore[typeddict-item]
    if "toolNames" in data:
        import aws_sdk_bedrock_agentcore.types.evaluation_tool_names
        out["tool_names"] = aws_sdk_bedrock_agentcore.types.evaluation_tool_names.deserialize_json(data["toolNames"])
    return out