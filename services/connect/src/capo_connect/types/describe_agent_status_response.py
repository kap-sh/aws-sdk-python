"""Generated from Smithy shape ``com.amazonaws.connect#DescribeAgentStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_status


class DescribeAgentStatusResponse(TypedDict, closed=True):
    agent_status: NotRequired["capo_connect.types.agent_status.AgentStatus"]
    """<p>The agent status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAgentStatusResponse) -> dict:
    out: dict = {}
    if "agent_status" in value:
        import capo_connect.types.agent_status

        out["AgentStatus"] = capo_connect.types.agent_status.serialize_json(
            value["agent_status"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAgentStatusResponse:
    out: DescribeAgentStatusResponse = {}  # type: ignore[typeddict-item]
    if "AgentStatus" in data:
        import capo_connect.types.agent_status

        out["agent_status"] = capo_connect.types.agent_status.deserialize_json(
            data["AgentStatus"]
        )
    return out
