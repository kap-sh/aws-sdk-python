"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent


class UpdateAgentResponse(TypedDict):
    agent: "aws_sdk_bedrock_agent.types.agent.Agent"
    """<p>Contains details about the agent that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent

    out["agent"] = aws_sdk_bedrock_agent.types.agent.serialize_json(value["agent"])
    return out


def deserialize_json(data: dict) -> UpdateAgentResponse:
    out: UpdateAgentResponse = {}  # type: ignore[typeddict-item]
    if "agent" in data:
        import aws_sdk_bedrock_agent.types.agent

        out["agent"] = aws_sdk_bedrock_agent.types.agent.deserialize_json(data["agent"])
    else:
        raise DeserializationError("UpdateAgentResponse.agent required")
    return out
