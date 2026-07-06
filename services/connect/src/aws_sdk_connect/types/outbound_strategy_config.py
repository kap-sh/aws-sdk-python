"""Generated from Smithy shape ``com.amazonaws.connect#OutboundStrategyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_first


class OutboundStrategyConfig(TypedDict, closed=True):
    agent_first: NotRequired["aws_sdk_connect.types.agent_first.AgentFirst"]
    """<p>The config of agent first outbound strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundStrategyConfig) -> dict:
    out: dict = {}
    if "agent_first" in value:
        import aws_sdk_connect.types.agent_first

        out["AgentFirst"] = aws_sdk_connect.types.agent_first.serialize_json(
            value["agent_first"]
        )
    return out


def deserialize_json(data: dict) -> OutboundStrategyConfig:
    out: OutboundStrategyConfig = {}  # type: ignore[typeddict-item]
    if "AgentFirst" in data:
        import aws_sdk_connect.types.agent_first

        out["agent_first"] = aws_sdk_connect.types.agent_first.deserialize_json(
            data["AgentFirst"]
        )
    return out
