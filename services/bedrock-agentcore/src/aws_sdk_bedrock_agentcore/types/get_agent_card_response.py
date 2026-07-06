"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetAgentCardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.agent_card
    import aws_sdk_bedrock_agentcore.types.http_response_code
    import aws_sdk_bedrock_agentcore.types.session_id


class GetAgentCardResponse(TypedDict, closed=True):
    runtime_session_id: NotRequired[
        "aws_sdk_bedrock_agentcore.types.session_id.SessionId"
    ]
    """<p>The ID of the session associated with the AgentCore Runtime agent.</p>"""
    agent_card: "aws_sdk_bedrock_agentcore.types.agent_card.AgentCard"
    """<p>An agent card document that contains metadata and capabilities for an AgentCore Runtime agent.</p>"""
    status_code: NotRequired[
        "aws_sdk_bedrock_agentcore.types.http_response_code.HttpResponseCode"
    ]
    """<p>The status code of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentCardResponse) -> dict:
    out: dict = {}
    out["agentCard"] = value["agent_card"]
    return out


def deserialize_json(data: dict) -> GetAgentCardResponse:
    out: GetAgentCardResponse = {}  # type: ignore[typeddict-item]
    if "agentCard" in data:
        out["agent_card"] = data["agentCard"]
    else:
        raise DeserializationError("GetAgentCardResponse.agent_card required")
    return out
