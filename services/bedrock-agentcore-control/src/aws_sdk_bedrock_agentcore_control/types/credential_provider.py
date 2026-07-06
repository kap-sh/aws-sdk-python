"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProvider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_api_key_credential_provider
    import aws_sdk_bedrock_agentcore_control.types.iam_credential_provider
    import aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider


class _CredentialProvider_oauthCredentialProvider(TypedDict, closed=True):
    oauthCredentialProvider: "aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider.OAuthCredentialProvider"


class _CredentialProvider_apiKeyCredentialProvider(TypedDict, closed=True):
    apiKeyCredentialProvider: "aws_sdk_bedrock_agentcore_control.types.gateway_api_key_credential_provider.GatewayApiKeyCredentialProvider"


class _CredentialProvider_iamCredentialProvider(TypedDict, closed=True):
    iamCredentialProvider: "aws_sdk_bedrock_agentcore_control.types.iam_credential_provider.IamCredentialProvider"


CredentialProvider: TypeAlias = (
    _CredentialProvider_oauthCredentialProvider
    | _CredentialProvider_apiKeyCredentialProvider
    | _CredentialProvider_iamCredentialProvider
)


# --- restJson1 ser/de ---
def serialize_json(value: CredentialProvider) -> dict:
    if "oauthCredentialProvider" in value:
        import aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider

        return {
            "oauthCredentialProvider": aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider.serialize_json(
                value["oauthCredentialProvider"]
            )
        }
    elif "apiKeyCredentialProvider" in value:
        import aws_sdk_bedrock_agentcore_control.types.gateway_api_key_credential_provider

        return {
            "apiKeyCredentialProvider": aws_sdk_bedrock_agentcore_control.types.gateway_api_key_credential_provider.serialize_json(
                value["apiKeyCredentialProvider"]
            )
        }
    elif "iamCredentialProvider" in value:
        import aws_sdk_bedrock_agentcore_control.types.iam_credential_provider

        return {
            "iamCredentialProvider": aws_sdk_bedrock_agentcore_control.types.iam_credential_provider.serialize_json(
                value["iamCredentialProvider"]
            )
        }
    else:
        raise SerializationError("CredentialProvider: no variant present")


def deserialize_json(data: dict) -> CredentialProvider:
    if "oauthCredentialProvider" in data:
        import aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider

        return {
            "oauthCredentialProvider": aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider.deserialize_json(
                data["oauthCredentialProvider"]
            )
        }
    elif "apiKeyCredentialProvider" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_api_key_credential_provider

        return {
            "apiKeyCredentialProvider": aws_sdk_bedrock_agentcore_control.types.gateway_api_key_credential_provider.deserialize_json(
                data["apiKeyCredentialProvider"]
            )
        }
    elif "iamCredentialProvider" in data:
        import aws_sdk_bedrock_agentcore_control.types.iam_credential_provider

        return {
            "iamCredentialProvider": aws_sdk_bedrock_agentcore_control.types.iam_credential_provider.deserialize_json(
                data["iamCredentialProvider"]
            )
        }
    else:
        raise DeserializationError("CredentialProvider: no recognized variant key")
