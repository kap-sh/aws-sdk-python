"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessEnvironmentArtifact``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.container_configuration


class _HarnessEnvironmentArtifact_containerConfiguration(TypedDict):
    containerConfiguration: "aws_sdk_bedrock_agentcore_control.types.container_configuration.ContainerConfiguration"


HarnessEnvironmentArtifact: TypeAlias = (
    _HarnessEnvironmentArtifact_containerConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessEnvironmentArtifact) -> dict:
    if "containerConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.container_configuration

        return {
            "containerConfiguration": aws_sdk_bedrock_agentcore_control.types.container_configuration.serialize_json(
                value["containerConfiguration"]
            )
        }
    else:
        raise SerializationError("HarnessEnvironmentArtifact: no variant present")


def deserialize_json(data: dict) -> HarnessEnvironmentArtifact:
    if "containerConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.container_configuration

        return {
            "containerConfiguration": aws_sdk_bedrock_agentcore_control.types.container_configuration.deserialize_json(
                data["containerConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessEnvironmentArtifact: no recognized variant key"
        )
