"""Generated from Smithy shape ``com.amazonaws.connect#AutoAcceptConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_first_callback_auto_accept
    import aws_sdk_connect.types.auto_accept
    import aws_sdk_connect.types.channel


class AutoAcceptConfig(TypedDict, closed=True):
    channel: "aws_sdk_connect.types.channel.Channel"
    """<p>The channel for this auto-accept configuration. Valid values: VOICE, CHAT, TASK, EMAIL.</p>"""
    auto_accept: "aws_sdk_connect.types.auto_accept.AutoAccept"
    """<p>Indicates whether auto-accept is enabled for this channel. When enabled, available agents are automatically connected to contacts from this channel.</p>"""
    agent_first_callback_auto_accept: NotRequired[
        "aws_sdk_connect.types.agent_first_callback_auto_accept.AgentFirstCallbackAutoAccept"
    ]
    """<p>Indicates whether auto-accept is enabled for agent-first callbacks. This setting only applies to the VOICE channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoAcceptConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.channel

    out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    out["AutoAccept"] = value.get("auto_accept", False)
    if "agent_first_callback_auto_accept" in value:
        out["AgentFirstCallbackAutoAccept"] = value["agent_first_callback_auto_accept"]
    return out


def deserialize_json(data: dict) -> AutoAcceptConfig:
    out: AutoAcceptConfig = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("AutoAcceptConfig.channel required")
    if "AutoAccept" in data:
        out["auto_accept"] = data["AutoAccept"]
    else:
        out["auto_accept"] = False
    if "AgentFirstCallbackAutoAccept" in data:
        out["agent_first_callback_auto_accept"] = data["AgentFirstCallbackAutoAccept"]
    return out
