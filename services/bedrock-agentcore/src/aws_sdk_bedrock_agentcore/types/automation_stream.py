"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AutomationStream``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.automation_stream_status
    import aws_sdk_bedrock_agentcore.types.browser_stream_endpoint


class AutomationStream(TypedDict, closed=True):
    stream_endpoint: (
        "aws_sdk_bedrock_agentcore.types.browser_stream_endpoint.BrowserStreamEndpoint"
    )
    """<p>The endpoint URL for the automation stream. This URL is used to establish a WebSocket connection to the stream for sending commands and receiving responses.</p>"""
    stream_status: "aws_sdk_bedrock_agentcore.types.automation_stream_status.AutomationStreamStatus"
    """<p>The current status of the automation stream. This indicates whether the stream is available for use. Possible values include ACTIVE, CONNECTING, and DISCONNECTED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationStream) -> dict:
    out: dict = {}
    out["streamEndpoint"] = value["stream_endpoint"]
    import aws_sdk_bedrock_agentcore.types.automation_stream_status

    out["streamStatus"] = (
        aws_sdk_bedrock_agentcore.types.automation_stream_status.serialize_json(
            value["stream_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomationStream:
    out: AutomationStream = {}  # type: ignore[typeddict-item]
    if "streamEndpoint" in data:
        out["stream_endpoint"] = data["streamEndpoint"]
    else:
        raise DeserializationError("AutomationStream.stream_endpoint required")
    if "streamStatus" in data:
        import aws_sdk_bedrock_agentcore.types.automation_stream_status

        out["stream_status"] = (
            aws_sdk_bedrock_agentcore.types.automation_stream_status.deserialize_json(
                data["streamStatus"]
            )
        )
    else:
        raise DeserializationError("AutomationStream.stream_status required")
    return out
