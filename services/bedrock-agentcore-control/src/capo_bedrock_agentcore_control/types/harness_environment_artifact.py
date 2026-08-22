"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessEnvironmentArtifact``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.container_configuration


class _HarnessEnvironmentArtifact_containerConfiguration(TypedDict, closed=True):
    containerConfiguration: "capo_bedrock_agentcore_control.types.container_configuration.ContainerConfiguration"


HarnessEnvironmentArtifact: TypeAlias = (
    _HarnessEnvironmentArtifact_containerConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessEnvironmentArtifact) -> dict:
    if "containerConfiguration" in value:
        import capo_bedrock_agentcore_control.types.container_configuration

        return {
            "containerConfiguration": capo_bedrock_agentcore_control.types.container_configuration.serialize_json(
                value["containerConfiguration"]
            )
        }
    else:
        raise SerializationError("HarnessEnvironmentArtifact: no variant present")


def deserialize_json(data: dict) -> HarnessEnvironmentArtifact:
    if data.get("containerConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.container_configuration

        return {
            "containerConfiguration": capo_bedrock_agentcore_control.types.container_configuration.deserialize_json(
                data["containerConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessEnvironmentArtifact: no recognized variant key"
        )
