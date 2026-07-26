"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteAgentRuntimeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.client_token


class DeleteAgentRuntimeRequest(TypedDict, closed=True):
    agent_runtime_id: (
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime to delete.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentRuntimeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentRuntimeRequest:
    out: DeleteAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
    return out
