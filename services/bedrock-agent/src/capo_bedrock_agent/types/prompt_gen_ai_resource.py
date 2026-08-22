"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptGenAiResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.prompt_agent_resource


class _PromptGenAiResource_agent(TypedDict, closed=True):
    agent: "capo_bedrock_agent.types.prompt_agent_resource.PromptAgentResource"


PromptGenAiResource: TypeAlias = _PromptGenAiResource_agent


# --- restJson1 ser/de ---
def serialize_json(value: PromptGenAiResource) -> dict:
    if "agent" in value:
        import capo_bedrock_agent.types.prompt_agent_resource

        return {
            "agent": capo_bedrock_agent.types.prompt_agent_resource.serialize_json(
                value["agent"]
            )
        }
    else:
        raise SerializationError("PromptGenAiResource: no variant present")


def deserialize_json(data: dict) -> PromptGenAiResource:
    if data.get("agent") is not None:
        import capo_bedrock_agent.types.prompt_agent_resource

        return {
            "agent": capo_bedrock_agent.types.prompt_agent_resource.deserialize_json(
                data["agent"]
            )
        }
    else:
        raise DeserializationError("PromptGenAiResource: no recognized variant key")
