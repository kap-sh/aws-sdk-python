"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessEnvironmentProviderRequest``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request


class _HarnessEnvironmentProviderRequest_agentCoreRuntimeEnvironment(TypedDict):
    agentCoreRuntimeEnvironment: "aws_sdk_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request.HarnessAgentCoreRuntimeEnvironmentRequest"


HarnessEnvironmentProviderRequest: TypeAlias = (
    _HarnessEnvironmentProviderRequest_agentCoreRuntimeEnvironment
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessEnvironmentProviderRequest) -> dict:
    if "agentCoreRuntimeEnvironment" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request

        return {
            "agentCoreRuntimeEnvironment": aws_sdk_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request.serialize_json(
                value["agentCoreRuntimeEnvironment"]
            )
        }
    else:
        raise SerializationError(
            "HarnessEnvironmentProviderRequest: no variant present"
        )


def deserialize_json(data: dict) -> HarnessEnvironmentProviderRequest:
    if "agentCoreRuntimeEnvironment" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request

        return {
            "agentCoreRuntimeEnvironment": aws_sdk_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request.deserialize_json(
                data["agentCoreRuntimeEnvironment"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessEnvironmentProviderRequest: no recognized variant key"
        )
