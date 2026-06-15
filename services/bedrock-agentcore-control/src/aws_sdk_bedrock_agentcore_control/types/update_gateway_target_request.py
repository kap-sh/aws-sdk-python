"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateGatewayTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier
    import aws_sdk_bedrock_agentcore_control.types.metadata_configuration
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint
    import aws_sdk_bedrock_agentcore_control.types.target_configuration
    import aws_sdk_bedrock_agentcore_control.types.target_description
    import aws_sdk_bedrock_agentcore_control.types.target_id
    import aws_sdk_bedrock_agentcore_control.types.target_name


class UpdateGatewayTargetRequest(TypedDict):
    gateway_identifier: (
        "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The unique identifier of the gateway associated with the target.</p>"""
    target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The unique identifier of the gateway target to update.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The updated name for the gateway target.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.target_description.TargetDescription"
    ]
    """<p>The updated description for the gateway target.</p>"""
    target_configuration: "aws_sdk_bedrock_agentcore_control.types.target_configuration.TargetConfiguration"
    credential_provider_configurations: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"
    ]
    """<p>The updated credential provider configurations for the gateway target.</p>"""
    metadata_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"
    ]
    """<p>Configuration for HTTP header and query parameter propagation to the gateway target.</p>"""
    private_endpoint: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    """<p>The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayTargetRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.target_configuration

    out["targetConfiguration"] = (
        aws_sdk_bedrock_agentcore_control.types.target_configuration.serialize_json(
            value["target_configuration"]
        )
    )
    if "credential_provider_configurations" in value:
        import aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations

        out["credentialProviderConfigurations"] = (
            aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.serialize_json(
                value["credential_provider_configurations"]
            )
        )
    if "metadata_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.metadata_configuration

        out["metadataConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.metadata_configuration.serialize_json(
                value["metadata_configuration"]
            )
        )
    if "private_endpoint" in value:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint

        out["privateEndpoint"] = (
            aws_sdk_bedrock_agentcore_control.types.private_endpoint.serialize_json(
                value["private_endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGatewayTargetRequest:
    out: UpdateGatewayTargetRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateGatewayTargetRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "targetConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.target_configuration

        out["target_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.target_configuration.deserialize_json(
                data["targetConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateGatewayTargetRequest.target_configuration required"
        )
    if "credentialProviderConfigurations" in data:
        import aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations

        out["credential_provider_configurations"] = (
            aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    if "metadataConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.metadata_configuration

        out["metadata_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.metadata_configuration.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    if "privateEndpoint" in data:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint

        out["private_endpoint"] = (
            aws_sdk_bedrock_agentcore_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    return out
