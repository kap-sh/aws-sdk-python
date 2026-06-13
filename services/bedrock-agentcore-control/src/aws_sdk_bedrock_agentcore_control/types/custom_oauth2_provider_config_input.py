"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomOauth2ProviderConfigInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type
    import aws_sdk_bedrock_agentcore_control.types.default_client_id_type
    import aws_sdk_bedrock_agentcore_control.types.default_client_secret_type
    import aws_sdk_bedrock_agentcore_control.types.oauth2_discovery
    import aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides
    import aws_sdk_bedrock_agentcore_control.types.secret_reference
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type

class CustomOauth2ProviderConfigInput(TypedDict):
    oauth_discovery: "aws_sdk_bedrock_agentcore_control.types.oauth2_discovery.Oauth2Discovery"
    """<p>The OAuth2 discovery information for the custom provider.</p>"""
    client_id: "aws_sdk_bedrock_agentcore_control.types.default_client_id_type.DefaultClientIdType"
    """<p>The client ID for the custom OAuth2 provider.</p>"""
    client_secret: "aws_sdk_bedrock_agentcore_control.types.default_client_secret_type.DefaultClientSecretType"
    """<p>The client secret for the custom OAuth2 provider.</p>"""
    client_secret_config: NotRequired["aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"]
    """<p>A reference to the AWS Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when <code>clientSecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    client_secret_source: NotRequired["aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"]
    """<p>The source type of the client secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>"""
    on_behalf_of_token_exchange_config: NotRequired["aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.OnBehalfOfTokenExchangeConfigType"]
    """<p>The configuration for on-behalf-of token exchange. This enables authentication flows that use RFC 8693 token exchange or RFC 7523 JWT authorization grants.</p>"""
    client_authentication_method: NotRequired["aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type.ClientAuthenticationMethodType"]
    """<p>The client authentication method to use when authenticating with the token endpoint.</p>"""
    private_endpoint: NotRequired["aws_sdk_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"]
    """<p>The default private endpoint for the custom OAuth2 provider, enabling secure connectivity through a VPC Lattice resource configuration.</p>"""
    private_endpoint_overrides: NotRequired["aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides.PrivateEndpointOverrides"]
    """<p>The private endpoint overrides for the custom OAuth2 provider configuration.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CustomOauth2ProviderConfigInput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.oauth2_discovery
    out["oauthDiscovery"] = aws_sdk_bedrock_agentcore_control.types.oauth2_discovery.serialize_json(value["oauth_discovery"])
    out["clientId"] = value.get("client_id", '')
    out["clientSecret"] = value.get("client_secret", '')
    if "client_secret_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference
        out["clientSecretConfig"] = aws_sdk_bedrock_agentcore_control.types.secret_reference.serialize_json(value["client_secret_config"])
    if "client_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type
        out["clientSecretSource"] = aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(value["client_secret_source"])
    if "on_behalf_of_token_exchange_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type
        out["onBehalfOfTokenExchangeConfig"] = aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.serialize_json(value["on_behalf_of_token_exchange_config"])
    if "client_authentication_method" in value:
        import aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type
        out["clientAuthenticationMethod"] = aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type.serialize_json(value["client_authentication_method"])
    if "private_endpoint" in value:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint
        out["privateEndpoint"] = aws_sdk_bedrock_agentcore_control.types.private_endpoint.serialize_json(value["private_endpoint"])
    if "private_endpoint_overrides" in value:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides
        out["privateEndpointOverrides"] = aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides.serialize_json(value["private_endpoint_overrides"])
    return out


def deserialize_json(data: dict) -> CustomOauth2ProviderConfigInput:
    out: CustomOauth2ProviderConfigInput = {}  # type: ignore[typeddict-item]
    if "oauthDiscovery" in data:
        import aws_sdk_bedrock_agentcore_control.types.oauth2_discovery
        out["oauth_discovery"] = aws_sdk_bedrock_agentcore_control.types.oauth2_discovery.deserialize_json(data["oauthDiscovery"])
    else:
        raise DeserializationError("CustomOauth2ProviderConfigInput.oauth_discovery required")
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        out["client_id"] = ''
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    else:
        out["client_secret"] = ''
    if "clientSecretConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference
        out["client_secret_config"] = aws_sdk_bedrock_agentcore_control.types.secret_reference.deserialize_json(data["clientSecretConfig"])
    if "clientSecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type
        out["client_secret_source"] = aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(data["clientSecretSource"])
    if "onBehalfOfTokenExchangeConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type
        out["on_behalf_of_token_exchange_config"] = aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.deserialize_json(data["onBehalfOfTokenExchangeConfig"])
    if "clientAuthenticationMethod" in data:
        import aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type
        out["client_authentication_method"] = aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type.deserialize_json(data["clientAuthenticationMethod"])
    if "privateEndpoint" in data:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint
        out["private_endpoint"] = aws_sdk_bedrock_agentcore_control.types.private_endpoint.deserialize_json(data["privateEndpoint"])
    if "privateEndpointOverrides" in data:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides
        out["private_endpoint_overrides"] = aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides.deserialize_json(data["privateEndpointOverrides"])
    return out