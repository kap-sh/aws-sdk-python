"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Finding``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.finding_type
    import aws_sdk_bedrock_agentcore_control.types.string

class Finding(TypedDict):
    type: NotRequired["aws_sdk_bedrock_agentcore_control.types.finding_type.FindingType"]
    """<p>The type or category of the finding. This classifies the finding as an error, warning, recommendation, or informational message to help users understand the severity and nature of the issue.</p>"""
    description: NotRequired["aws_sdk_bedrock_agentcore_control.types.string.String"]
    """<p>A human-readable description of the finding. This provides detailed information about the issue, recommendation, or validation result to help users understand and address the finding. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_bedrock_agentcore_control.types.finding_type
        out["type"] = aws_sdk_bedrock_agentcore_control.types.finding_type.serialize_json(value["type"])
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agentcore_control.types.finding_type
        out["type"] = aws_sdk_bedrock_agentcore_control.types.finding_type.deserialize_json(data["type"])
    if "description" in data:
        out["description"] = data["description"]
    return out