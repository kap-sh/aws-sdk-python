"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionGroupInvocationOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.action_group_output_string
    import aws_sdk_bedrock_agent_runtime.types.metadata

class ActionGroupInvocationOutput(TypedDict):
    text: NotRequired["aws_sdk_bedrock_agent_runtime.types.action_group_output_string.ActionGroupOutputString"]
    """<p>The JSON-formatted string returned by the API invoked by the action group.</p>"""
    metadata: NotRequired["aws_sdk_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the action group output.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupInvocationOutput) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.metadata
        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.serialize_json(value["metadata"])
    return out


def deserialize_json(data: dict) -> ActionGroupInvocationOutput:
    out: ActionGroupInvocationOutput = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    if "metadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.metadata
        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.deserialize_json(data["metadata"])
    return out