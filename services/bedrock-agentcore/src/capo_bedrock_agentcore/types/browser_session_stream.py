"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserSessionStream``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.automation_stream
    import capo_bedrock_agentcore.types.live_view_stream


class BrowserSessionStream(TypedDict, closed=True):
    automation_stream: "capo_bedrock_agentcore.types.automation_stream.AutomationStream"
    """<p>The stream that enables programmatic control of the browser. This stream allows agents to perform actions such as navigating to URLs, clicking elements, and filling forms.</p>"""
    live_view_stream: NotRequired[
        "capo_bedrock_agentcore.types.live_view_stream.LiveViewStream"
    ]
    """<p>The stream that provides a visual representation of the browser content. This stream allows agents to observe the current state of the browser, including rendered web pages and visual elements.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSessionStream) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.automation_stream

    out["automationStream"] = (
        capo_bedrock_agentcore.types.automation_stream.serialize_json(
            value["automation_stream"]
        )
    )
    if "live_view_stream" in value:
        import capo_bedrock_agentcore.types.live_view_stream

        out["liveViewStream"] = (
            capo_bedrock_agentcore.types.live_view_stream.serialize_json(
                value["live_view_stream"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrowserSessionStream:
    out: BrowserSessionStream = {}  # type: ignore[typeddict-item]
    if data.get("automationStream") is not None:
        import capo_bedrock_agentcore.types.automation_stream

        out["automation_stream"] = (
            capo_bedrock_agentcore.types.automation_stream.deserialize_json(
                data["automationStream"]
            )
        )
    else:
        raise DeserializationError("BrowserSessionStream.automation_stream required")
    if data.get("liveViewStream") is not None:
        import capo_bedrock_agentcore.types.live_view_stream

        out["live_view_stream"] = (
            capo_bedrock_agentcore.types.live_view_stream.deserialize_json(
                data["liveViewStream"]
            )
        )
    return out
