"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.numerical_version


class GetAgentVersionRequest(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion"
    """<p>The version of the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentVersionRequest:
    out: GetAgentVersionRequest = {}  # type: ignore[typeddict-item]
    return out
