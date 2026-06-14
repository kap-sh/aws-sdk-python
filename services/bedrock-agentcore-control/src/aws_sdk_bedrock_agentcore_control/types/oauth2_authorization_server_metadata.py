"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Oauth2AuthorizationServerMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorization_endpoint_type
    import aws_sdk_bedrock_agentcore_control.types.issuer_url_type
    import aws_sdk_bedrock_agentcore_control.types.response_list_type
    import aws_sdk_bedrock_agentcore_control.types.token_endpoint_auth_methods_type
    import aws_sdk_bedrock_agentcore_control.types.token_endpoint_type


class Oauth2AuthorizationServerMetadata(TypedDict):
    issuer: "aws_sdk_bedrock_agentcore_control.types.issuer_url_type.IssuerUrlType"
    """<p>The issuer URL for the OAuth2 authorization server.</p>"""
    authorization_endpoint: "aws_sdk_bedrock_agentcore_control.types.authorization_endpoint_type.AuthorizationEndpointType"
    """<p>The authorization endpoint URL for the OAuth2 authorization server.</p>"""
    token_endpoint: (
        "aws_sdk_bedrock_agentcore_control.types.token_endpoint_type.TokenEndpointType"
    )
    """<p>The token endpoint URL for the OAuth2 authorization server.</p>"""
    response_types: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.response_list_type.ResponseListType"
    ]
    """<p>The supported response types for the OAuth2 authorization server.</p>"""
    token_endpoint_auth_methods: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.token_endpoint_auth_methods_type.TokenEndpointAuthMethodsType"
    ]
    """<p>The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2AuthorizationServerMetadata) -> dict:
    out: dict = {}
    out["issuer"] = value["issuer"]
    out["authorizationEndpoint"] = value["authorization_endpoint"]
    out["tokenEndpoint"] = value["token_endpoint"]
    if "response_types" in value:
        import aws_sdk_bedrock_agentcore_control.types.response_list_type

        out["responseTypes"] = (
            aws_sdk_bedrock_agentcore_control.types.response_list_type.serialize_json(
                value["response_types"]
            )
        )
    if "token_endpoint_auth_methods" in value:
        import aws_sdk_bedrock_agentcore_control.types.token_endpoint_auth_methods_type

        out["tokenEndpointAuthMethods"] = (
            aws_sdk_bedrock_agentcore_control.types.token_endpoint_auth_methods_type.serialize_json(
                value["token_endpoint_auth_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> Oauth2AuthorizationServerMetadata:
    out: Oauth2AuthorizationServerMetadata = {}  # type: ignore[typeddict-item]
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    else:
        raise DeserializationError("Oauth2AuthorizationServerMetadata.issuer required")
    if "authorizationEndpoint" in data:
        out["authorization_endpoint"] = data["authorizationEndpoint"]
    else:
        raise DeserializationError(
            "Oauth2AuthorizationServerMetadata.authorization_endpoint required"
        )
    if "tokenEndpoint" in data:
        out["token_endpoint"] = data["tokenEndpoint"]
    else:
        raise DeserializationError(
            "Oauth2AuthorizationServerMetadata.token_endpoint required"
        )
    if "responseTypes" in data:
        import aws_sdk_bedrock_agentcore_control.types.response_list_type

        out["response_types"] = (
            aws_sdk_bedrock_agentcore_control.types.response_list_type.deserialize_json(
                data["responseTypes"]
            )
        )
    if "tokenEndpointAuthMethods" in data:
        import aws_sdk_bedrock_agentcore_control.types.token_endpoint_auth_methods_type

        out["token_endpoint_auth_methods"] = (
            aws_sdk_bedrock_agentcore_control.types.token_endpoint_auth_methods_type.deserialize_json(
                data["tokenEndpointAuthMethods"]
            )
        )
    return out
