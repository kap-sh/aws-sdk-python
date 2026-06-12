"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptGenAiResource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.prompt_agent_resource


class _PromptGenAiResource_agent(TypedDict):
    agent: "aws_sdk_bedrock_agent.types.prompt_agent_resource.PromptAgentResource"


PromptGenAiResource: TypeAlias = _PromptGenAiResource_agent


# --- restJson1 ser/de ---
def serialize_json(value: PromptGenAiResource) -> dict:
    if "agent" in value:
        import aws_sdk_bedrock_agent.types.prompt_agent_resource

        return {
            "agent": aws_sdk_bedrock_agent.types.prompt_agent_resource.serialize_json(
                value["agent"]
            )
        }
    else:
        raise SerializationError("PromptGenAiResource: no variant present")


def deserialize_json(data: dict) -> PromptGenAiResource:
    if "agent" in data:
        import aws_sdk_bedrock_agent.types.prompt_agent_resource

        return {
            "agent": aws_sdk_bedrock_agent.types.prompt_agent_resource.deserialize_json(
                data["agent"]
            )
        }
    else:
        raise DeserializationError("PromptGenAiResource: no recognized variant key")
