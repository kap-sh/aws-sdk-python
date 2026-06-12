"""Generated from Smithy shape ``com.amazonaws.connect#DescribeAgentStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status


class DescribeAgentStatusResponse(TypedDict):
    agent_status: NotRequired["aws_sdk_connect.types.agent_status.AgentStatus"]
    """<p>The agent status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAgentStatusResponse) -> dict:
    out: dict = {}
    if "agent_status" in value:
        import aws_sdk_connect.types.agent_status

        out["AgentStatus"] = aws_sdk_connect.types.agent_status.serialize_json(
            value["agent_status"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAgentStatusResponse:
    out: DescribeAgentStatusResponse = {}  # type: ignore[typeddict-item]
    if "AgentStatus" in data:
        import aws_sdk_connect.types.agent_status

        out["agent_status"] = aws_sdk_connect.types.agent_status.deserialize_json(
            data["AgentStatus"]
        )
    return out
