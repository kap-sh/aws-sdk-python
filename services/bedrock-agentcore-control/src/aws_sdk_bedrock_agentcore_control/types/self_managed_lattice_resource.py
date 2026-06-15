"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SelfManagedLatticeResource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_configuration_identifier


class _SelfManagedLatticeResource_resourceConfigurationIdentifier(TypedDict):
    resourceConfigurationIdentifier: "aws_sdk_bedrock_agentcore_control.types.resource_configuration_identifier.ResourceConfigurationIdentifier"


SelfManagedLatticeResource: TypeAlias = (
    _SelfManagedLatticeResource_resourceConfigurationIdentifier
)


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedLatticeResource) -> dict:
    if "resourceConfigurationIdentifier" in value:
        return {
            "resourceConfigurationIdentifier": value["resourceConfigurationIdentifier"]
        }
    else:
        raise SerializationError("SelfManagedLatticeResource: no variant present")


def deserialize_json(data: dict) -> SelfManagedLatticeResource:
    if "resourceConfigurationIdentifier" in data:
        return {
            "resourceConfigurationIdentifier": data["resourceConfigurationIdentifier"]
        }
    else:
        raise DeserializationError(
            "SelfManagedLatticeResource: no recognized variant key"
        )
