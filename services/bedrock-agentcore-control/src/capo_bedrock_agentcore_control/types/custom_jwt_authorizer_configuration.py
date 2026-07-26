"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomJWTAuthorizerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.allowed_audience_list
    import capo_bedrock_agentcore_control.types.allowed_clients_list
    import capo_bedrock_agentcore_control.types.allowed_scopes_type
    import capo_bedrock_agentcore_control.types.custom_claim_validations_type
    import capo_bedrock_agentcore_control.types.discovery_url
    import capo_bedrock_agentcore_control.types.private_endpoint
    import capo_bedrock_agentcore_control.types.private_endpoint_overrides


class CustomJWTAuthorizerConfiguration(TypedDict, closed=True):
    discovery_url: "capo_bedrock_agentcore_control.types.discovery_url.DiscoveryUrl"
    """<p>This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.</p>"""
    allowed_audience: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_audience_list.AllowedAudienceList"
    ]
    """<p>Represents individual audience values that are validated in the incoming JWT token validation process.</p>"""
    allowed_clients: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_clients_list.AllowedClientsList"
    ]
    """<p>Represents individual client IDs that are validated in the incoming JWT token validation process.</p>"""
    allowed_scopes: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_scopes_type.AllowedScopesType"
    ]
    """<p>An array of scopes that are allowed to access the token.</p>"""
    custom_claims: NotRequired[
        "capo_bedrock_agentcore_control.types.custom_claim_validations_type.CustomClaimValidationsType"
    ]
    """<p>An array of objects that define a custom claim validation name, value, and operation </p>"""
    private_endpoint: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    private_endpoint_overrides: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint_overrides.PrivateEndpointOverrides"
    ]
    """<p>The private endpoint overrides for the custom JWT authorizer configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomJWTAuthorizerConfiguration) -> dict:
    out: dict = {}
    out["discoveryUrl"] = value["discovery_url"]
    if "allowed_audience" in value:
        import capo_bedrock_agentcore_control.types.allowed_audience_list

        out["allowedAudience"] = (
            capo_bedrock_agentcore_control.types.allowed_audience_list.serialize_json(
                value["allowed_audience"]
            )
        )
    if "allowed_clients" in value:
        import capo_bedrock_agentcore_control.types.allowed_clients_list

        out["allowedClients"] = (
            capo_bedrock_agentcore_control.types.allowed_clients_list.serialize_json(
                value["allowed_clients"]
            )
        )
    if "allowed_scopes" in value:
        import capo_bedrock_agentcore_control.types.allowed_scopes_type

        out["allowedScopes"] = (
            capo_bedrock_agentcore_control.types.allowed_scopes_type.serialize_json(
                value["allowed_scopes"]
            )
        )
    if "custom_claims" in value:
        import capo_bedrock_agentcore_control.types.custom_claim_validations_type

        out["customClaims"] = (
            capo_bedrock_agentcore_control.types.custom_claim_validations_type.serialize_json(
                value["custom_claims"]
            )
        )
    if "private_endpoint" in value:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["privateEndpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.serialize_json(
                value["private_endpoint"]
            )
        )
    if "private_endpoint_overrides" in value:
        import capo_bedrock_agentcore_control.types.private_endpoint_overrides

        out["privateEndpointOverrides"] = (
            capo_bedrock_agentcore_control.types.private_endpoint_overrides.serialize_json(
                value["private_endpoint_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomJWTAuthorizerConfiguration:
    out: CustomJWTAuthorizerConfiguration = {}  # type: ignore[typeddict-item]
    if "discoveryUrl" in data:
        out["discovery_url"] = data["discoveryUrl"]
    else:
        raise DeserializationError(
            "CustomJWTAuthorizerConfiguration.discovery_url required"
        )
    if "allowedAudience" in data:
        import capo_bedrock_agentcore_control.types.allowed_audience_list

        out["allowed_audience"] = (
            capo_bedrock_agentcore_control.types.allowed_audience_list.deserialize_json(
                data["allowedAudience"]
            )
        )
    if "allowedClients" in data:
        import capo_bedrock_agentcore_control.types.allowed_clients_list

        out["allowed_clients"] = (
            capo_bedrock_agentcore_control.types.allowed_clients_list.deserialize_json(
                data["allowedClients"]
            )
        )
    if "allowedScopes" in data:
        import capo_bedrock_agentcore_control.types.allowed_scopes_type

        out["allowed_scopes"] = (
            capo_bedrock_agentcore_control.types.allowed_scopes_type.deserialize_json(
                data["allowedScopes"]
            )
        )
    if "customClaims" in data:
        import capo_bedrock_agentcore_control.types.custom_claim_validations_type

        out["custom_claims"] = (
            capo_bedrock_agentcore_control.types.custom_claim_validations_type.deserialize_json(
                data["customClaims"]
            )
        )
    if "privateEndpoint" in data:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["private_endpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    if "privateEndpointOverrides" in data:
        import capo_bedrock_agentcore_control.types.private_endpoint_overrides

        out["private_endpoint_overrides"] = (
            capo_bedrock_agentcore_control.types.private_endpoint_overrides.deserialize_json(
                data["privateEndpointOverrides"]
            )
        )
    return out
