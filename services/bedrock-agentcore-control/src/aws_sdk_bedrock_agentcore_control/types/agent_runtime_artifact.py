"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeArtifact``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.code_configuration
    import aws_sdk_bedrock_agentcore_control.types.container_configuration


class _AgentRuntimeArtifact_containerConfiguration(TypedDict):
    containerConfiguration: "aws_sdk_bedrock_agentcore_control.types.container_configuration.ContainerConfiguration"


class _AgentRuntimeArtifact_codeConfiguration(TypedDict):
    codeConfiguration: (
        "aws_sdk_bedrock_agentcore_control.types.code_configuration.CodeConfiguration"
    )


AgentRuntimeArtifact: TypeAlias = (
    _AgentRuntimeArtifact_containerConfiguration
    | _AgentRuntimeArtifact_codeConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeArtifact) -> dict:
    if "containerConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.container_configuration

        return {
            "containerConfiguration": aws_sdk_bedrock_agentcore_control.types.container_configuration.serialize_json(
                value["containerConfiguration"]
            )
        }
    elif "codeConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.code_configuration

        return {
            "codeConfiguration": aws_sdk_bedrock_agentcore_control.types.code_configuration.serialize_json(
                value["codeConfiguration"]
            )
        }
    else:
        raise SerializationError("AgentRuntimeArtifact: no variant present")


def deserialize_json(data: dict) -> AgentRuntimeArtifact:
    if "containerConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.container_configuration

        return {
            "containerConfiguration": aws_sdk_bedrock_agentcore_control.types.container_configuration.deserialize_json(
                data["containerConfiguration"]
            )
        }
    elif "codeConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.code_configuration

        return {
            "codeConfiguration": aws_sdk_bedrock_agentcore_control.types.code_configuration.deserialize_json(
                data["codeConfiguration"]
            )
        }
    else:
        raise DeserializationError("AgentRuntimeArtifact: no recognized variant key")
