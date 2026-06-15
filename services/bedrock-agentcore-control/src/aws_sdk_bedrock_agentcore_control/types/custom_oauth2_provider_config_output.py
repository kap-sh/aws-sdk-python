"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomOauth2ProviderConfigOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type
    import aws_sdk_bedrock_agentcore_control.types.client_id_type
    import aws_sdk_bedrock_agentcore_control.types.oauth2_discovery
    import aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides


class CustomOauth2ProviderConfigOutput(TypedDict):
    oauth_discovery: (
        "aws_sdk_bedrock_agentcore_control.types.oauth2_discovery.Oauth2Discovery"
    )
    """<p>The OAuth2 discovery information for the custom provider.</p>"""
    client_id: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_id_type.ClientIdType"
    ]
    """<p>The client ID for the custom OAuth2 provider.</p>"""
    private_endpoint: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    """<p>The default private endpoint for the custom OAuth2 provider, enabling secure connectivity through a VPC Lattice resource configuration.</p>"""
    private_endpoint_overrides: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides.PrivateEndpointOverrides"
    ]
    """<p>The private endpoint overrides for the custom OAuth2 provider configuration.</p>"""
    on_behalf_of_token_exchange_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.OnBehalfOfTokenExchangeConfigType"
    ]
    """<p>The configuration for on-behalf-of token exchange.</p>"""
    client_authentication_method: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type.ClientAuthenticationMethodType"
    ]
    """<p>The client authentication method used when authenticating with the token endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomOauth2ProviderConfigOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.oauth2_discovery

    out["oauthDiscovery"] = (
        aws_sdk_bedrock_agentcore_control.types.oauth2_discovery.serialize_json(
            value["oauth_discovery"]
        )
    )
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "private_endpoint" in value:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint

        out["privateEndpoint"] = (
            aws_sdk_bedrock_agentcore_control.types.private_endpoint.serialize_json(
                value["private_endpoint"]
            )
        )
    if "private_endpoint_overrides" in value:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides

        out["privateEndpointOverrides"] = (
            aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides.serialize_json(
                value["private_endpoint_overrides"]
            )
        )
    if "on_behalf_of_token_exchange_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type

        out["onBehalfOfTokenExchangeConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.serialize_json(
                value["on_behalf_of_token_exchange_config"]
            )
        )
    if "client_authentication_method" in value:
        import aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type

        out["clientAuthenticationMethod"] = (
            aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type.serialize_json(
                value["client_authentication_method"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomOauth2ProviderConfigOutput:
    out: CustomOauth2ProviderConfigOutput = {}  # type: ignore[typeddict-item]
    if "oauthDiscovery" in data:
        import aws_sdk_bedrock_agentcore_control.types.oauth2_discovery

        out["oauth_discovery"] = (
            aws_sdk_bedrock_agentcore_control.types.oauth2_discovery.deserialize_json(
                data["oauthDiscovery"]
            )
        )
    else:
        raise DeserializationError(
            "CustomOauth2ProviderConfigOutput.oauth_discovery required"
        )
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    if "privateEndpoint" in data:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint

        out["private_endpoint"] = (
            aws_sdk_bedrock_agentcore_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    if "privateEndpointOverrides" in data:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides

        out["private_endpoint_overrides"] = (
            aws_sdk_bedrock_agentcore_control.types.private_endpoint_overrides.deserialize_json(
                data["privateEndpointOverrides"]
            )
        )
    if "onBehalfOfTokenExchangeConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type

        out["on_behalf_of_token_exchange_config"] = (
            aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.deserialize_json(
                data["onBehalfOfTokenExchangeConfig"]
            )
        )
    if "clientAuthenticationMethod" in data:
        import aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type

        out["client_authentication_method"] = (
            aws_sdk_bedrock_agentcore_control.types.client_authentication_method_type.deserialize_json(
                data["clientAuthenticationMethod"]
            )
        )
    return out
