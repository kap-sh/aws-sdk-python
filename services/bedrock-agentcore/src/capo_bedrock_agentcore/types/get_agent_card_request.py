"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetAgentCardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.session_type


class GetAgentCardRequest(TypedDict, closed=True):
    runtime_session_id: NotRequired[
        "capo_bedrock_agentcore.types.session_type.SessionType"
    ]
    """<p>The session ID that the AgentCore Runtime agent is using. </p>"""
    agent_runtime_arn: "str"
    """<p>The ARN of the AgentCore Runtime agent for which you want to get the A2A agent card.</p>"""
    qualifier: NotRequired["str"]
    """<p>Optional qualifier to specify an agent alias, such as <code>prod</code>code&gt; or <code>dev</code>. If you don't provide a value, the DEFAULT alias is used. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentCardRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentCardRequest:
    out: GetAgentCardRequest = {}  # type: ignore[typeddict-item]
    return out
