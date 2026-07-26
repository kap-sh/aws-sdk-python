"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessEnvironmentProvider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment


class _HarnessEnvironmentProvider_agentCoreRuntimeEnvironment(TypedDict, closed=True):
    agentCoreRuntimeEnvironment: "capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment.HarnessAgentCoreRuntimeEnvironment"


HarnessEnvironmentProvider: TypeAlias = (
    _HarnessEnvironmentProvider_agentCoreRuntimeEnvironment
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessEnvironmentProvider) -> dict:
    if "agentCoreRuntimeEnvironment" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment

        return {
            "agentCoreRuntimeEnvironment": capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment.serialize_json(
                value["agentCoreRuntimeEnvironment"]
            )
        }
    else:
        raise SerializationError("HarnessEnvironmentProvider: no variant present")


def deserialize_json(data: dict) -> HarnessEnvironmentProvider:
    if "agentCoreRuntimeEnvironment" in data:
        import capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment

        return {
            "agentCoreRuntimeEnvironment": capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment.deserialize_json(
                data["agentCoreRuntimeEnvironment"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessEnvironmentProvider: no recognized variant key"
        )
