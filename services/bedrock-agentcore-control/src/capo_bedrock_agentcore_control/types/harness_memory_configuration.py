"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessMemoryConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration


class _HarnessMemoryConfiguration_agentCoreMemoryConfiguration(TypedDict, closed=True):
    agentCoreMemoryConfiguration: "capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration.HarnessAgentCoreMemoryConfiguration"


HarnessMemoryConfiguration: TypeAlias = (
    _HarnessMemoryConfiguration_agentCoreMemoryConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMemoryConfiguration) -> dict:
    if "agentCoreMemoryConfiguration" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration

        return {
            "agentCoreMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration.serialize_json(
                value["agentCoreMemoryConfiguration"]
            )
        }
    else:
        raise SerializationError("HarnessMemoryConfiguration: no variant present")


def deserialize_json(data: dict) -> HarnessMemoryConfiguration:
    if "agentCoreMemoryConfiguration" in data:
        import capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration

        return {
            "agentCoreMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration.deserialize_json(
                data["agentCoreMemoryConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessMemoryConfiguration: no recognized variant key"
        )
