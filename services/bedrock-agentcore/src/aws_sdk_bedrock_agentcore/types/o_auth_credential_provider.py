"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OAuthCredentialProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.o_auth_credential_provider_arn
    import aws_sdk_bedrock_agentcore.types.o_auth_custom_parameters
    import aws_sdk_bedrock_agentcore.types.o_auth_default_return_url
    import aws_sdk_bedrock_agentcore.types.o_auth_grant_type
    import aws_sdk_bedrock_agentcore.types.o_auth_scopes


class OAuthCredentialProvider(TypedDict, closed=True):
    provider_arn: "aws_sdk_bedrock_agentcore.types.o_auth_credential_provider_arn.OAuthCredentialProviderArn"
    """<p>The ARN of the OAuth 2.0 credential provider in AgentCore Identity.</p>"""
    scopes: "aws_sdk_bedrock_agentcore.types.o_auth_scopes.OAuthScopes"
    """<p>The OAuth 2.0 scopes to request when obtaining an access token.</p>"""
    custom_parameters: NotRequired[
        "aws_sdk_bedrock_agentcore.types.o_auth_custom_parameters.OAuthCustomParameters"
    ]
    """<p>Additional custom parameters to include in the OAuth 2.0 token request.</p>"""
    grant_type: "aws_sdk_bedrock_agentcore.types.o_auth_grant_type.OAuthGrantType"
    """<p>The OAuth 2.0 grant type to use for authentication.</p>"""
    default_return_url: NotRequired[
        "aws_sdk_bedrock_agentcore.types.o_auth_default_return_url.OAuthDefaultReturnUrl"
    ]
    """<p>The default return URL for the OAuth 2.0 authorization flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthCredentialProvider) -> dict:
    out: dict = {}
    out["providerArn"] = value["provider_arn"]
    import aws_sdk_bedrock_agentcore.types.o_auth_scopes

    out["scopes"] = aws_sdk_bedrock_agentcore.types.o_auth_scopes.serialize_json(
        value["scopes"]
    )
    if "custom_parameters" in value:
        import aws_sdk_bedrock_agentcore.types.o_auth_custom_parameters

        out["customParameters"] = (
            aws_sdk_bedrock_agentcore.types.o_auth_custom_parameters.serialize_json(
                value["custom_parameters"]
            )
        )
    import aws_sdk_bedrock_agentcore.types.o_auth_grant_type

    out["grantType"] = aws_sdk_bedrock_agentcore.types.o_auth_grant_type.serialize_json(
        value.get("grant_type", "CLIENT_CREDENTIALS")
    )
    if "default_return_url" in value:
        out["defaultReturnUrl"] = value["default_return_url"]
    return out


def deserialize_json(data: dict) -> OAuthCredentialProvider:
    out: OAuthCredentialProvider = {}  # type: ignore[typeddict-item]
    if "providerArn" in data:
        out["provider_arn"] = data["providerArn"]
    else:
        raise DeserializationError("OAuthCredentialProvider.provider_arn required")
    if "scopes" in data:
        import aws_sdk_bedrock_agentcore.types.o_auth_scopes

        out["scopes"] = aws_sdk_bedrock_agentcore.types.o_auth_scopes.deserialize_json(
            data["scopes"]
        )
    else:
        raise DeserializationError("OAuthCredentialProvider.scopes required")
    if "customParameters" in data:
        import aws_sdk_bedrock_agentcore.types.o_auth_custom_parameters

        out["custom_parameters"] = (
            aws_sdk_bedrock_agentcore.types.o_auth_custom_parameters.deserialize_json(
                data["customParameters"]
            )
        )
    if "grantType" in data:
        import aws_sdk_bedrock_agentcore.types.o_auth_grant_type

        out["grant_type"] = (
            aws_sdk_bedrock_agentcore.types.o_auth_grant_type.deserialize_json(
                data["grantType"]
            )
        )
    else:
        out["grant_type"] = "CLIENT_CREDENTIALS"
    if "defaultReturnUrl" in data:
        out["default_return_url"] = data["defaultReturnUrl"]
    return out
