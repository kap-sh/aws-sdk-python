"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetGatewayTargetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorization_data
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.gateway_arn
    import aws_sdk_bedrock_agentcore_control.types.metadata_configuration
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint_managed_resources
    import aws_sdk_bedrock_agentcore_control.types.status_reasons
    import aws_sdk_bedrock_agentcore_control.types.target_configuration
    import aws_sdk_bedrock_agentcore_control.types.target_description
    import aws_sdk_bedrock_agentcore_control.types.target_id
    import aws_sdk_bedrock_agentcore_control.types.target_name
    import aws_sdk_bedrock_agentcore_control.types.target_protocol_type
    import aws_sdk_bedrock_agentcore_control.types.target_status


class GetGatewayTargetResponse(TypedDict):
    gateway_arn: "aws_sdk_bedrock_agentcore_control.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""
    target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The unique identifier of the gateway target.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway target was created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway target was last updated.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.target_status.TargetStatus"
    """<p>The current status of the gateway target.</p>"""
    status_reasons: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.status_reasons.StatusReasons"
    ]
    """<p>The reasons for the current status of the gateway target.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The name of the gateway target.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.target_description.TargetDescription"
    ]
    """<p>The description of the gateway target.</p>"""
    target_configuration: "aws_sdk_bedrock_agentcore_control.types.target_configuration.TargetConfiguration"
    credential_provider_configurations: "aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"
    """<p>The credential provider configurations for the gateway target.</p>"""
    last_synchronized_at: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The last synchronization of the target.</p>"""
    metadata_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"
    ]
    """<p>The metadata configuration for HTTP header and query parameter propagation for the retrieved gateway target.</p>"""
    private_endpoint: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    """<p>The private endpoint configuration for the gateway target.</p>"""
    private_endpoint_managed_resources: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.private_endpoint_managed_resources.PrivateEndpointManagedResources"
    ]
    """<p>The managed resources created by the gateway for private endpoint connectivity.</p>"""
    authorization_data: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.authorization_data.AuthorizationData"
    ]
    """<p>OAuth2 authorization data for the gateway target. This data is returned when a target is configured with a credential provider with authorization code grant type and requires user federation.</p>"""
    protocol_type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.target_protocol_type.TargetProtocolType"
    ]
    """<p>The protocol type of the gateway target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayTargetResponse) -> dict:
    out: dict = {}
    out["gatewayArn"] = value["gateway_arn"]
    out["targetId"] = value["target_id"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.target_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.target_status.serialize_json(
            value["status"]
        )
    )
    if "status_reasons" in value:
        import aws_sdk_bedrock_agentcore_control.types.status_reasons

        out["statusReasons"] = (
            aws_sdk_bedrock_agentcore_control.types.status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.target_configuration

    out["targetConfiguration"] = (
        aws_sdk_bedrock_agentcore_control.types.target_configuration.serialize_json(
            value["target_configuration"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations

    out["credentialProviderConfigurations"] = (
        aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.serialize_json(
            value["credential_provider_configurations"]
        )
    )
    if "last_synchronized_at" in value:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["lastSynchronizedAt"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
                value["last_synchronized_at"]
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
    if "private_endpoint_managed_resources" in value:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint_managed_resources

        out["privateEndpointManagedResources"] = (
            aws_sdk_bedrock_agentcore_control.types.private_endpoint_managed_resources.serialize_json(
                value["private_endpoint_managed_resources"]
            )
        )
    if "authorization_data" in value:
        import aws_sdk_bedrock_agentcore_control.types.authorization_data

        out["authorizationData"] = (
            aws_sdk_bedrock_agentcore_control.types.authorization_data.serialize_json(
                value["authorization_data"]
            )
        )
    if "protocol_type" in value:
        import aws_sdk_bedrock_agentcore_control.types.target_protocol_type

        out["protocolType"] = (
            aws_sdk_bedrock_agentcore_control.types.target_protocol_type.serialize_json(
                value["protocol_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGatewayTargetResponse:
    out: GetGatewayTargetResponse = {}  # type: ignore[typeddict-item]
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("GetGatewayTargetResponse.gateway_arn required")
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError("GetGatewayTargetResponse.target_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetGatewayTargetResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetGatewayTargetResponse.updated_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.target_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.target_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetGatewayTargetResponse.status required")
    if "statusReasons" in data:
        import aws_sdk_bedrock_agentcore_control.types.status_reasons

        out["status_reasons"] = (
            aws_sdk_bedrock_agentcore_control.types.status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetGatewayTargetResponse.name required")
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
            "GetGatewayTargetResponse.target_configuration required"
        )
    if "credentialProviderConfigurations" in data:
        import aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations

        out["credential_provider_configurations"] = (
            aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "GetGatewayTargetResponse.credential_provider_configurations required"
        )
    if "lastSynchronizedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["last_synchronized_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastSynchronizedAt"]
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
    if "privateEndpointManagedResources" in data:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint_managed_resources

        out["private_endpoint_managed_resources"] = (
            aws_sdk_bedrock_agentcore_control.types.private_endpoint_managed_resources.deserialize_json(
                data["privateEndpointManagedResources"]
            )
        )
    if "authorizationData" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorization_data

        out["authorization_data"] = (
            aws_sdk_bedrock_agentcore_control.types.authorization_data.deserialize_json(
                data["authorizationData"]
            )
        )
    if "protocolType" in data:
        import aws_sdk_bedrock_agentcore_control.types.target_protocol_type

        out["protocol_type"] = (
            aws_sdk_bedrock_agentcore_control.types.target_protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    return out
