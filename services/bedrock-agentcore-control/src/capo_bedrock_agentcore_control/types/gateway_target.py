"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorization_data
    import capo_bedrock_agentcore_control.types.credential_provider_configurations
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.gateway_arn
    import capo_bedrock_agentcore_control.types.metadata_configuration
    import capo_bedrock_agentcore_control.types.private_endpoint
    import capo_bedrock_agentcore_control.types.private_endpoint_managed_resources
    import capo_bedrock_agentcore_control.types.status_reasons
    import capo_bedrock_agentcore_control.types.target_configuration
    import capo_bedrock_agentcore_control.types.target_description
    import capo_bedrock_agentcore_control.types.target_id
    import capo_bedrock_agentcore_control.types.target_name
    import capo_bedrock_agentcore_control.types.target_protocol_type
    import capo_bedrock_agentcore_control.types.target_status


class GatewayTarget(TypedDict, closed=True):
    gateway_arn: "capo_bedrock_agentcore_control.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway target.</p>"""
    target_id: "capo_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The target ID.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The date and time at which the target was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The date and time at which the target was updated.</p>"""
    status: "capo_bedrock_agentcore_control.types.target_status.TargetStatus"
    """<p>The status of the gateway target.</p>"""
    status_reasons: NotRequired[
        "capo_bedrock_agentcore_control.types.status_reasons.StatusReasons"
    ]
    """<p>The status reasons for the target status.</p>"""
    name: "capo_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The name of the gateway target.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.target_description.TargetDescription"
    ]
    """<p>The description for the gateway target.</p>"""
    target_configuration: (
        "capo_bedrock_agentcore_control.types.target_configuration.TargetConfiguration"
    )
    credential_provider_configurations: "capo_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"
    """<p>The provider configurations.</p>"""
    last_synchronized_at: NotRequired[
        "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The last synchronization time.</p>"""
    metadata_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"
    ]
    """<p>The metadata configuration for HTTP header and query parameter propagation to and from this gateway target.</p>"""
    private_endpoint: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    private_endpoint_managed_resources: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint_managed_resources.PrivateEndpointManagedResources"
    ]
    """<p>A list of managed resources created by the gateway for private endpoint connectivity. These resources are created in your account when you use a managed VPC Lattice resource configuration.</p>"""
    authorization_data: NotRequired[
        "capo_bedrock_agentcore_control.types.authorization_data.AuthorizationData"
    ]
    """<p>OAuth2 authorization data for the gateway target. This data is returned when a target is configured with a credential provider with authorization code grant type and requires user federation.</p>"""
    protocol_type: NotRequired[
        "capo_bedrock_agentcore_control.types.target_protocol_type.TargetProtocolType"
    ]
    """<p>The protocol type of the gateway target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayTarget) -> dict:
    out: dict = {}
    out["gatewayArn"] = value["gateway_arn"]
    out["targetId"] = value["target_id"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.target_status

    out["status"] = capo_bedrock_agentcore_control.types.target_status.serialize_json(
        value["status"]
    )
    if "status_reasons" in value:
        import capo_bedrock_agentcore_control.types.status_reasons

        out["statusReasons"] = (
            capo_bedrock_agentcore_control.types.status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.target_configuration

    out["targetConfiguration"] = (
        capo_bedrock_agentcore_control.types.target_configuration.serialize_json(
            value["target_configuration"]
        )
    )
    import capo_bedrock_agentcore_control.types.credential_provider_configurations

    out["credentialProviderConfigurations"] = (
        capo_bedrock_agentcore_control.types.credential_provider_configurations.serialize_json(
            value["credential_provider_configurations"]
        )
    )
    if "last_synchronized_at" in value:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["lastSynchronizedAt"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
                value["last_synchronized_at"]
            )
        )
    if "metadata_configuration" in value:
        import capo_bedrock_agentcore_control.types.metadata_configuration

        out["metadataConfiguration"] = (
            capo_bedrock_agentcore_control.types.metadata_configuration.serialize_json(
                value["metadata_configuration"]
            )
        )
    if "private_endpoint" in value:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["privateEndpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.serialize_json(
                value["private_endpoint"]
            )
        )
    if "private_endpoint_managed_resources" in value:
        import capo_bedrock_agentcore_control.types.private_endpoint_managed_resources

        out["privateEndpointManagedResources"] = (
            capo_bedrock_agentcore_control.types.private_endpoint_managed_resources.serialize_json(
                value["private_endpoint_managed_resources"]
            )
        )
    if "authorization_data" in value:
        import capo_bedrock_agentcore_control.types.authorization_data

        out["authorizationData"] = (
            capo_bedrock_agentcore_control.types.authorization_data.serialize_json(
                value["authorization_data"]
            )
        )
    if "protocol_type" in value:
        import capo_bedrock_agentcore_control.types.target_protocol_type

        out["protocolType"] = (
            capo_bedrock_agentcore_control.types.target_protocol_type.serialize_json(
                value["protocol_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GatewayTarget:
    out: GatewayTarget = {}  # type: ignore[typeddict-item]
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("GatewayTarget.gateway_arn required")
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError("GatewayTarget.target_id required")
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GatewayTarget.created_at required")
    if "updatedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GatewayTarget.updated_at required")
    if "status" in data:
        import capo_bedrock_agentcore_control.types.target_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.target_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GatewayTarget.status required")
    if "statusReasons" in data:
        import capo_bedrock_agentcore_control.types.status_reasons

        out["status_reasons"] = (
            capo_bedrock_agentcore_control.types.status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GatewayTarget.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "targetConfiguration" in data:
        import capo_bedrock_agentcore_control.types.target_configuration

        out["target_configuration"] = (
            capo_bedrock_agentcore_control.types.target_configuration.deserialize_json(
                data["targetConfiguration"]
            )
        )
    else:
        raise DeserializationError("GatewayTarget.target_configuration required")
    if "credentialProviderConfigurations" in data:
        import capo_bedrock_agentcore_control.types.credential_provider_configurations

        out["credential_provider_configurations"] = (
            capo_bedrock_agentcore_control.types.credential_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "GatewayTarget.credential_provider_configurations required"
        )
    if "lastSynchronizedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_synchronized_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastSynchronizedAt"]
            )
        )
    if "metadataConfiguration" in data:
        import capo_bedrock_agentcore_control.types.metadata_configuration

        out["metadata_configuration"] = (
            capo_bedrock_agentcore_control.types.metadata_configuration.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    if "privateEndpoint" in data:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["private_endpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    if "privateEndpointManagedResources" in data:
        import capo_bedrock_agentcore_control.types.private_endpoint_managed_resources

        out["private_endpoint_managed_resources"] = (
            capo_bedrock_agentcore_control.types.private_endpoint_managed_resources.deserialize_json(
                data["privateEndpointManagedResources"]
            )
        )
    if "authorizationData" in data:
        import capo_bedrock_agentcore_control.types.authorization_data

        out["authorization_data"] = (
            capo_bedrock_agentcore_control.types.authorization_data.deserialize_json(
                data["authorizationData"]
            )
        )
    if "protocolType" in data:
        import capo_bedrock_agentcore_control.types.target_protocol_type

        out["protocol_type"] = (
            capo_bedrock_agentcore_control.types.target_protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    return out
