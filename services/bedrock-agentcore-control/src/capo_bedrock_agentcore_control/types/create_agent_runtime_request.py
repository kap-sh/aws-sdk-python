"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateAgentRuntimeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_artifact
    import capo_bedrock_agentcore_control.types.agent_runtime_name
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.environment_variables_map
    import capo_bedrock_agentcore_control.types.filesystem_configurations
    import capo_bedrock_agentcore_control.types.lifecycle_configuration
    import capo_bedrock_agentcore_control.types.network_configuration
    import capo_bedrock_agentcore_control.types.protocol_configuration
    import capo_bedrock_agentcore_control.types.request_header_configuration
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.tags_map


class CreateAgentRuntimeRequest(TypedDict, closed=True):
    agent_runtime_name: (
        "capo_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName"
    )
    """<p>The name of the AgentCore Runtime.</p>"""
    agent_runtime_artifact: "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact"
    """<p>The artifact of the AgentCore Runtime.</p>"""
    role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The IAM role ARN that provides permissions for the AgentCore Runtime.</p>"""
    network_configuration: "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
    """<p>The network configuration for the AgentCore Runtime.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the AgentCore Runtime.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The authorizer configuration for the AgentCore Runtime.</p>"""
    request_header_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
    ]
    """<p>Configuration for HTTP request headers that will be passed through to the runtime.</p>"""
    protocol_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
    ]
    lifecycle_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
    ]
    """<p>The life cycle configuration for the AgentCore Runtime.</p>"""
    environment_variables: NotRequired[
        "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables to set in the AgentCore Runtime environment.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
    ]
    """<p>The filesystem configurations to mount into the AgentCore Runtime. Use filesystem configurations to provide persistent storage to your AgentCore Runtime sessions.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the agent runtime. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentRuntimeRequest) -> dict:
    out: dict = {}
    out["agentRuntimeName"] = value["agent_runtime_name"]
    import capo_bedrock_agentcore_control.types.agent_runtime_artifact

    out["agentRuntimeArtifact"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_artifact.serialize_json(
            value["agent_runtime_artifact"]
        )
    )
    out["roleArn"] = value["role_arn"]
    import capo_bedrock_agentcore_control.types.network_configuration

    out["networkConfiguration"] = (
        capo_bedrock_agentcore_control.types.network_configuration.serialize_json(
            value["network_configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "authorizer_configuration" in value:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "request_header_configuration" in value:
        import capo_bedrock_agentcore_control.types.request_header_configuration

        out["requestHeaderConfiguration"] = (
            capo_bedrock_agentcore_control.types.request_header_configuration.serialize_json(
                value["request_header_configuration"]
            )
        )
    if "protocol_configuration" in value:
        import capo_bedrock_agentcore_control.types.protocol_configuration

        out["protocolConfiguration"] = (
            capo_bedrock_agentcore_control.types.protocol_configuration.serialize_json(
                value["protocol_configuration"]
            )
        )
    if "lifecycle_configuration" in value:
        import capo_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycleConfiguration"] = (
            capo_bedrock_agentcore_control.types.lifecycle_configuration.serialize_json(
                value["lifecycle_configuration"]
            )
        )
    if "environment_variables" in value:
        import capo_bedrock_agentcore_control.types.environment_variables_map

        out["environmentVariables"] = (
            capo_bedrock_agentcore_control.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
    if "filesystem_configurations" in value:
        import capo_bedrock_agentcore_control.types.filesystem_configurations

        out["filesystemConfigurations"] = (
            capo_bedrock_agentcore_control.types.filesystem_configurations.serialize_json(
                value["filesystem_configurations"]
            )
        )
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateAgentRuntimeRequest:
    out: CreateAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
    if "agentRuntimeName" in data:
        out["agent_runtime_name"] = data["agentRuntimeName"]
    else:
        raise DeserializationError(
            "CreateAgentRuntimeRequest.agent_runtime_name required"
        )
    if "agentRuntimeArtifact" in data:
        import capo_bedrock_agentcore_control.types.agent_runtime_artifact

        out["agent_runtime_artifact"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_artifact.deserialize_json(
                data["agentRuntimeArtifact"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAgentRuntimeRequest.agent_runtime_artifact required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateAgentRuntimeRequest.role_arn required")
    if "networkConfiguration" in data:
        import capo_bedrock_agentcore_control.types.network_configuration

        out["network_configuration"] = (
            capo_bedrock_agentcore_control.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAgentRuntimeRequest.network_configuration required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "authorizerConfiguration" in data:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if "requestHeaderConfiguration" in data:
        import capo_bedrock_agentcore_control.types.request_header_configuration

        out["request_header_configuration"] = (
            capo_bedrock_agentcore_control.types.request_header_configuration.deserialize_json(
                data["requestHeaderConfiguration"]
            )
        )
    if "protocolConfiguration" in data:
        import capo_bedrock_agentcore_control.types.protocol_configuration

        out["protocol_configuration"] = (
            capo_bedrock_agentcore_control.types.protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    if "lifecycleConfiguration" in data:
        import capo_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_bedrock_agentcore_control.types.lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    if "environmentVariables" in data:
        import capo_bedrock_agentcore_control.types.environment_variables_map

        out["environment_variables"] = (
            capo_bedrock_agentcore_control.types.environment_variables_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    if "filesystemConfigurations" in data:
        import capo_bedrock_agentcore_control.types.filesystem_configurations

        out["filesystem_configurations"] = (
            capo_bedrock_agentcore_control.types.filesystem_configurations.deserialize_json(
                data["filesystemConfigurations"]
            )
        )
    if "tags" in data:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
