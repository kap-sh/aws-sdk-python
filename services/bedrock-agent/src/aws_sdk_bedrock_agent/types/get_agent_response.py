"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent


class GetAgentResponse(TypedDict, closed=True):
    agent: "aws_sdk_bedrock_agent.types.agent.Agent"
    """<p>Contains details about the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent

    out["agent"] = aws_sdk_bedrock_agent.types.agent.serialize_json(value["agent"])
    return out


def deserialize_json(data: dict) -> GetAgentResponse:
    out: GetAgentResponse = {}  # type: ignore[typeddict-item]
    if "agent" in data:
        import aws_sdk_bedrock_agent.types.agent

        out["agent"] = aws_sdk_bedrock_agent.types.agent.deserialize_json(data["agent"])
    else:
        raise DeserializationError("GetAgentResponse.agent required")
    return out
