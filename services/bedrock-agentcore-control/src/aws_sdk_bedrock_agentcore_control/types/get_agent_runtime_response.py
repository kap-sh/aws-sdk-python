"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetAgentRuntimeResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_name
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_status
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.environment_variables_map
    import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations
    import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration
    import aws_sdk_bedrock_agentcore_control.types.network_configuration
    import aws_sdk_bedrock_agentcore_control.types.protocol_configuration
    import aws_sdk_bedrock_agentcore_control.types.request_header_configuration
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.runtime_metadata_configuration
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_details

class GetAgentRuntimeResponse(TypedDict):
    agent_runtime_arn: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime.</p>"""
    agent_runtime_name: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName"
    """<p>The name of the AgentCore Runtime.</p>"""
    agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    """<p>The unique identifier of the AgentCore Runtime.</p>"""
    agent_runtime_version: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    """<p>The version of the AgentCore Runtime.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime was created.</p>"""
    last_updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime was last updated.</p>"""
    role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The IAM role ARN that provides permissions for the AgentCore Runtime.</p>"""
    network_configuration: "aws_sdk_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
    """<p>The network configuration for the AgentCore Runtime.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus"
    """<p>The current status of the AgentCore Runtime.</p>"""
    lifecycle_configuration: "aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
    """<p>The life cycle configuration for the AgentCore Runtime.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the AgentCore Runtime is in a failed state.</p>"""
    description: NotRequired["aws_sdk_bedrock_agentcore_control.types.description.Description"]
    """<p>The description of the AgentCore Runtime.</p>"""
    workload_identity_details: NotRequired["aws_sdk_bedrock_agentcore_control.types.workload_identity_details.WorkloadIdentityDetails"]
    """<p>The workload identity details for the AgentCore Runtime.</p>"""
    agent_runtime_artifact: NotRequired["aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact"]
    """<p>The artifact of the AgentCore Runtime.</p>"""
    protocol_configuration: NotRequired["aws_sdk_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"]
    environment_variables: NotRequired["aws_sdk_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"]
    """<p>Environment variables set in the AgentCore Runtime environment.</p>"""
    authorizer_configuration: NotRequired["aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"]
    """<p>The authorizer configuration for the AgentCore Runtime.</p>"""
    request_header_configuration: NotRequired["aws_sdk_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"]
    """<p>Configuration for HTTP request headers that will be passed through to the runtime.</p>"""
    metadata_configuration: NotRequired["aws_sdk_bedrock_agentcore_control.types.runtime_metadata_configuration.RuntimeMetadataConfiguration"]
    """<p>Configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.</p>"""
    filesystem_configurations: NotRequired["aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"]
    """<p>The filesystem configurations mounted into the AgentCore Runtime.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRuntimeResponse) -> dict:
    out: dict = {}
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    out["agentRuntimeName"] = value["agent_runtime_name"]
    out["agentRuntimeId"] = value["agent_runtime_id"]
    out["agentRuntimeVersion"] = value["agent_runtime_version"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["created_at"])
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["lastUpdatedAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["last_updated_at"])
    out["roleArn"] = value["role_arn"]
    import aws_sdk_bedrock_agentcore_control.types.network_configuration
    out["networkConfiguration"] = aws_sdk_bedrock_agentcore_control.types.network_configuration.serialize_json(value["network_configuration"])
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_status.serialize_json(value["status"])
    import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration
    out["lifecycleConfiguration"] = aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.serialize_json(value["lifecycle_configuration"])
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "description" in value:
        out["description"] = value["description"]
    if "workload_identity_details" in value:
        import aws_sdk_bedrock_agentcore_control.types.workload_identity_details
        out["workloadIdentityDetails"] = aws_sdk_bedrock_agentcore_control.types.workload_identity_details.serialize_json(value["workload_identity_details"])
    if "agent_runtime_artifact" in value:
        import aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact
        out["agentRuntimeArtifact"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact.serialize_json(value["agent_runtime_artifact"])
    if "protocol_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.protocol_configuration
        out["protocolConfiguration"] = aws_sdk_bedrock_agentcore_control.types.protocol_configuration.serialize_json(value["protocol_configuration"])
    if "environment_variables" in value:
        import aws_sdk_bedrock_agentcore_control.types.environment_variables_map
        out["environmentVariables"] = aws_sdk_bedrock_agentcore_control.types.environment_variables_map.serialize_json(value["environment_variables"])
    if "authorizer_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
        out["authorizerConfiguration"] = aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(value["authorizer_configuration"])
    if "request_header_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.request_header_configuration
        out["requestHeaderConfiguration"] = aws_sdk_bedrock_agentcore_control.types.request_header_configuration.serialize_json(value["request_header_configuration"])
    if "metadata_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.runtime_metadata_configuration
        out["metadataConfiguration"] = aws_sdk_bedrock_agentcore_control.types.runtime_metadata_configuration.serialize_json(value["metadata_configuration"])
    if "filesystem_configurations" in value:
        import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations
        out["filesystemConfigurations"] = aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.serialize_json(value["filesystem_configurations"])
    return out


def deserialize_json(data: dict) -> GetAgentRuntimeResponse:
    out: GetAgentRuntimeResponse = {}  # type: ignore[typeddict-item]
    if "agentRuntimeArn" in data:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        raise DeserializationError("GetAgentRuntimeResponse.agent_runtime_arn required")
    if "agentRuntimeName" in data:
        out["agent_runtime_name"] = data["agentRuntimeName"]
    else:
        raise DeserializationError("GetAgentRuntimeResponse.agent_runtime_name required")
    if "agentRuntimeId" in data:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    else:
        raise DeserializationError("GetAgentRuntimeResponse.agent_runtime_id required")
    if "agentRuntimeVersion" in data:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    else:
        raise DeserializationError("GetAgentRuntimeResponse.agent_runtime_version required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("GetAgentRuntimeResponse.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["last_updated_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["lastUpdatedAt"])
    else:
        raise DeserializationError("GetAgentRuntimeResponse.last_updated_at required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetAgentRuntimeResponse.role_arn required")
    if "networkConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.network_configuration
        out["network_configuration"] = aws_sdk_bedrock_agentcore_control.types.network_configuration.deserialize_json(data["networkConfiguration"])
    else:
        raise DeserializationError("GetAgentRuntimeResponse.network_configuration required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_runtime_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("GetAgentRuntimeResponse.status required")
    if "lifecycleConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration
        out["lifecycle_configuration"] = aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.deserialize_json(data["lifecycleConfiguration"])
    else:
        raise DeserializationError("GetAgentRuntimeResponse.lifecycle_configuration required")
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "description" in data:
        out["description"] = data["description"]
    if "workloadIdentityDetails" in data:
        import aws_sdk_bedrock_agentcore_control.types.workload_identity_details
        out["workload_identity_details"] = aws_sdk_bedrock_agentcore_control.types.workload_identity_details.deserialize_json(data["workloadIdentityDetails"])
    if "agentRuntimeArtifact" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact
        out["agent_runtime_artifact"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact.deserialize_json(data["agentRuntimeArtifact"])
    if "protocolConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.protocol_configuration
        out["protocol_configuration"] = aws_sdk_bedrock_agentcore_control.types.protocol_configuration.deserialize_json(data["protocolConfiguration"])
    if "environmentVariables" in data:
        import aws_sdk_bedrock_agentcore_control.types.environment_variables_map
        out["environment_variables"] = aws_sdk_bedrock_agentcore_control.types.environment_variables_map.deserialize_json(data["environmentVariables"])
    if "authorizerConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
        out["authorizer_configuration"] = aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(data["authorizerConfiguration"])
    if "requestHeaderConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.request_header_configuration
        out["request_header_configuration"] = aws_sdk_bedrock_agentcore_control.types.request_header_configuration.deserialize_json(data["requestHeaderConfiguration"])
    if "metadataConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.runtime_metadata_configuration
        out["metadata_configuration"] = aws_sdk_bedrock_agentcore_control.types.runtime_metadata_configuration.deserialize_json(data["metadataConfiguration"])
    if "filesystemConfigurations" in data:
        import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations
        out["filesystem_configurations"] = aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.deserialize_json(data["filesystemConfigurations"])
    return out