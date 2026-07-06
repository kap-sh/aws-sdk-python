"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HttpTargetConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.runtime_target_configuration


class _HttpTargetConfiguration_agentcoreRuntime(TypedDict, closed=True):
    agentcoreRuntime: "aws_sdk_bedrock_agentcore_control.types.runtime_target_configuration.RuntimeTargetConfiguration"


HttpTargetConfiguration: TypeAlias = _HttpTargetConfiguration_agentcoreRuntime


# --- restJson1 ser/de ---
def serialize_json(value: HttpTargetConfiguration) -> dict:
    if "agentcoreRuntime" in value:
        import aws_sdk_bedrock_agentcore_control.types.runtime_target_configuration

        return {
            "agentcoreRuntime": aws_sdk_bedrock_agentcore_control.types.runtime_target_configuration.serialize_json(
                value["agentcoreRuntime"]
            )
        }
    else:
        raise SerializationError("HttpTargetConfiguration: no variant present")


def deserialize_json(data: dict) -> HttpTargetConfiguration:
    if "agentcoreRuntime" in data:
        import aws_sdk_bedrock_agentcore_control.types.runtime_target_configuration

        return {
            "agentcoreRuntime": aws_sdk_bedrock_agentcore_control.types.runtime_target_configuration.deserialize_json(
                data["agentcoreRuntime"]
            )
        }
    else:
        raise DeserializationError("HttpTargetConfiguration: no recognized variant key")
