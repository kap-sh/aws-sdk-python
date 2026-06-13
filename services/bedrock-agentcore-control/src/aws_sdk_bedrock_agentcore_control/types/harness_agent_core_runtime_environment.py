"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreRuntimeEnvironment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn
    import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations
    import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration
    import aws_sdk_bedrock_agentcore_control.types.network_configuration

class HarnessAgentCoreRuntimeEnvironment(TypedDict):
    agent_runtime_arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
    """<p>The ARN of the underlying AgentCore Runtime.</p>"""
    agent_runtime_name: "str"
    """<p>The name of the underlying AgentCore Runtime.</p>"""
    agent_runtime_id: "str"
    """<p>The ID of the underlying AgentCore Runtime.</p>"""
    lifecycle_configuration: "aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
    network_configuration: "aws_sdk_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
    filesystem_configurations: NotRequired["aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"]
    """<p>The filesystem configurations for the runtime environment.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreRuntimeEnvironment) -> dict:
    out: dict = {}
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    out["agentRuntimeName"] = value["agent_runtime_name"]
    out["agentRuntimeId"] = value["agent_runtime_id"]
    import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration
    out["lifecycleConfiguration"] = aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.serialize_json(value["lifecycle_configuration"])
    import aws_sdk_bedrock_agentcore_control.types.network_configuration
    out["networkConfiguration"] = aws_sdk_bedrock_agentcore_control.types.network_configuration.serialize_json(value["network_configuration"])
    if "filesystem_configurations" in value:
        import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations
        out["filesystemConfigurations"] = aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.serialize_json(value["filesystem_configurations"])
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreRuntimeEnvironment:
    out: HarnessAgentCoreRuntimeEnvironment = {}  # type: ignore[typeddict-item]
    if "agentRuntimeArn" in data:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        raise DeserializationError("HarnessAgentCoreRuntimeEnvironment.agent_runtime_arn required")
    if "agentRuntimeName" in data:
        out["agent_runtime_name"] = data["agentRuntimeName"]
    else:
        raise DeserializationError("HarnessAgentCoreRuntimeEnvironment.agent_runtime_name required")
    if "agentRuntimeId" in data:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    else:
        raise DeserializationError("HarnessAgentCoreRuntimeEnvironment.agent_runtime_id required")
    if "lifecycleConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration
        out["lifecycle_configuration"] = aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.deserialize_json(data["lifecycleConfiguration"])
    else:
        raise DeserializationError("HarnessAgentCoreRuntimeEnvironment.lifecycle_configuration required")
    if "networkConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.network_configuration
        out["network_configuration"] = aws_sdk_bedrock_agentcore_control.types.network_configuration.deserialize_json(data["networkConfiguration"])
    else:
        raise DeserializationError("HarnessAgentCoreRuntimeEnvironment.network_configuration required")
    if "filesystemConfigurations" in data:
        import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations
        out["filesystem_configurations"] = aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.deserialize_json(data["filesystemConfigurations"])
    return out