"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserSessionStream``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.automation_stream
    import aws_sdk_bedrock_agentcore.types.live_view_stream


class BrowserSessionStream(TypedDict):
    automation_stream: (
        "aws_sdk_bedrock_agentcore.types.automation_stream.AutomationStream"
    )
    """<p>The stream that enables programmatic control of the browser. This stream allows agents to perform actions such as navigating to URLs, clicking elements, and filling forms.</p>"""
    live_view_stream: NotRequired[
        "aws_sdk_bedrock_agentcore.types.live_view_stream.LiveViewStream"
    ]
    """<p>The stream that provides a visual representation of the browser content. This stream allows agents to observe the current state of the browser, including rendered web pages and visual elements.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSessionStream) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.automation_stream

    out["automationStream"] = (
        aws_sdk_bedrock_agentcore.types.automation_stream.serialize_json(
            value["automation_stream"]
        )
    )
    if "live_view_stream" in value:
        import aws_sdk_bedrock_agentcore.types.live_view_stream

        out["liveViewStream"] = (
            aws_sdk_bedrock_agentcore.types.live_view_stream.serialize_json(
                value["live_view_stream"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrowserSessionStream:
    out: BrowserSessionStream = {}  # type: ignore[typeddict-item]
    if "automationStream" in data:
        import aws_sdk_bedrock_agentcore.types.automation_stream

        out["automation_stream"] = (
            aws_sdk_bedrock_agentcore.types.automation_stream.deserialize_json(
                data["automationStream"]
            )
        )
    else:
        raise DeserializationError("BrowserSessionStream.automation_stream required")
    if "liveViewStream" in data:
        import aws_sdk_bedrock_agentcore.types.live_view_stream

        out["live_view_stream"] = (
            aws_sdk_bedrock_agentcore.types.live_view_stream.deserialize_json(
                data["liveViewStream"]
            )
        )
    return out
