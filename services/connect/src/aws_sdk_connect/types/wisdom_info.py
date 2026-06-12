"""Generated from Smithy shape ``com.amazonaws.connect#WisdomInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.ai_agents
    import aws_sdk_connect.types.arn


class WisdomInfo(TypedDict):
    session_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the Wisdom session.</p>"""
    ai_agents: NotRequired["aws_sdk_connect.types.ai_agents.AiAgents"]
    """<p>The array of AI agents involved in the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WisdomInfo) -> dict:
    out: dict = {}
    if "session_arn" in value:
        out["SessionArn"] = value["session_arn"]
    if "ai_agents" in value:
        import aws_sdk_connect.types.ai_agents

        out["AiAgents"] = aws_sdk_connect.types.ai_agents.serialize_json(
            value["ai_agents"]
        )
    return out


def deserialize_json(data: dict) -> WisdomInfo:
    out: WisdomInfo = {}  # type: ignore[typeddict-item]
    if "SessionArn" in data:
        out["session_arn"] = data["SessionArn"]
    if "AiAgents" in data:
        import aws_sdk_connect.types.ai_agents

        out["ai_agents"] = aws_sdk_connect.types.ai_agents.deserialize_json(
            data["AiAgents"]
        )
    return out
