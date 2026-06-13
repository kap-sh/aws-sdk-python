"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteAgentSpaceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_space_id


class DeleteAgentSpaceOutput(TypedDict):
    agent_space_id: NotRequired[
        "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId"
    ]
    """<p>The unique identifier of the deleted agent space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentSpaceOutput) -> dict:
    out: dict = {}
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> DeleteAgentSpaceOutput:
    out: DeleteAgentSpaceOutput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    return out
