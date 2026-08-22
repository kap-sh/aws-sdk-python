"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeArtifact``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.code_configuration
    import capo_bedrock_agentcore_control.types.container_configuration


class _AgentRuntimeArtifact_containerConfiguration(TypedDict, closed=True):
    containerConfiguration: "capo_bedrock_agentcore_control.types.container_configuration.ContainerConfiguration"


class _AgentRuntimeArtifact_codeConfiguration(TypedDict, closed=True):
    codeConfiguration: (
        "capo_bedrock_agentcore_control.types.code_configuration.CodeConfiguration"
    )


AgentRuntimeArtifact: TypeAlias = (
    _AgentRuntimeArtifact_containerConfiguration
    | _AgentRuntimeArtifact_codeConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeArtifact) -> dict:
    if "containerConfiguration" in value:
        import capo_bedrock_agentcore_control.types.container_configuration

        return {
            "containerConfiguration": capo_bedrock_agentcore_control.types.container_configuration.serialize_json(
                value["containerConfiguration"]
            )
        }
    elif "codeConfiguration" in value:
        import capo_bedrock_agentcore_control.types.code_configuration

        return {
            "codeConfiguration": capo_bedrock_agentcore_control.types.code_configuration.serialize_json(
                value["codeConfiguration"]
            )
        }
    else:
        raise SerializationError("AgentRuntimeArtifact: no variant present")


def deserialize_json(data: dict) -> AgentRuntimeArtifact:
    if data.get("containerConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.container_configuration

        return {
            "containerConfiguration": capo_bedrock_agentcore_control.types.container_configuration.deserialize_json(
                data["containerConfiguration"]
            )
        }
    elif data.get("codeConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.code_configuration

        return {
            "codeConfiguration": capo_bedrock_agentcore_control.types.code_configuration.deserialize_json(
                data["codeConfiguration"]
            )
        }
    else:
        raise DeserializationError("AgentRuntimeArtifact: no recognized variant key")
