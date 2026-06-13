"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AutomationStreamUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.automation_stream_status

class AutomationStreamUpdate(TypedDict):
    stream_status: NotRequired["aws_sdk_bedrock_agentcore.types.automation_stream_status.AutomationStreamStatus"]
    """<p>The status of the automation stream.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AutomationStreamUpdate) -> dict:
    out: dict = {}
    if "stream_status" in value:
        import aws_sdk_bedrock_agentcore.types.automation_stream_status
        out["streamStatus"] = aws_sdk_bedrock_agentcore.types.automation_stream_status.serialize_json(value["stream_status"])
    return out


def deserialize_json(data: dict) -> AutomationStreamUpdate:
    out: AutomationStreamUpdate = {}  # type: ignore[typeddict-item]
    if "streamStatus" in data:
        import aws_sdk_bedrock_agentcore.types.automation_stream_status
        out["stream_status"] = aws_sdk_bedrock_agentcore.types.automation_stream_status.deserialize_json(data["streamStatus"])
    return out