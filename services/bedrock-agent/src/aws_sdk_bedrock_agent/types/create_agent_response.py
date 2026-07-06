"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent


class CreateAgentResponse(TypedDict, closed=True):
    agent: "aws_sdk_bedrock_agent.types.agent.Agent"
    """<p>Contains details about the agent created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent

    out["agent"] = aws_sdk_bedrock_agent.types.agent.serialize_json(value["agent"])
    return out


def deserialize_json(data: dict) -> CreateAgentResponse:
    out: CreateAgentResponse = {}  # type: ignore[typeddict-item]
    if "agent" in data:
        import aws_sdk_bedrock_agent.types.agent

        out["agent"] = aws_sdk_bedrock_agent.types.agent.deserialize_json(data["agent"])
    else:
        raise DeserializationError("CreateAgentResponse.agent required")
    return out
