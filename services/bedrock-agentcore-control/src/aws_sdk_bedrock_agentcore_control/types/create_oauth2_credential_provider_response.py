"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateOauth2CredentialProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_arn_type
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output
    import aws_sdk_bedrock_agentcore_control.types.secret
    import aws_sdk_bedrock_agentcore_control.types.secret_json_key_type
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type
    import aws_sdk_bedrock_agentcore_control.types.status


class CreateOauth2CredentialProviderResponse(TypedDict, closed=True):
    client_secret_arn: "aws_sdk_bedrock_agentcore_control.types.secret.Secret"
    """<p>The Amazon Resource Name (ARN) of the client secret in AWS Secrets Manager.</p>"""
    client_secret_json_key: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the client secret value from the AWS Secrets Manager secret.</p>"""
    client_secret_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the client secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in AWS Secrets Manager.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the OAuth2 credential provider.</p>"""
    credential_provider_arn: "aws_sdk_bedrock_agentcore_control.types.credential_provider_arn_type.CredentialProviderArnType"
    """<p>The Amazon Resource Name (ARN) of the OAuth2 credential provider.</p>"""
    callback_url: NotRequired["str"]
    """<p>Callback URL to register on the OAuth2 credential provider as an allowed callback URL. This URL is where the OAuth2 authorization server redirects users after they complete the authorization flow.</p>"""
    oauth2_provider_config_output: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output.Oauth2ProviderConfigOutput"
    ]
    status: NotRequired["aws_sdk_bedrock_agentcore_control.types.status.Status"]
    """<p>The current status of the OAuth2 credential provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOauth2CredentialProviderResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.secret

    out["clientSecretArn"] = (
        aws_sdk_bedrock_agentcore_control.types.secret.serialize_json(
            value["client_secret_arn"]
        )
    )
    if "client_secret_json_key" in value:
        out["clientSecretJsonKey"] = value["client_secret_json_key"]
    if "client_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["clientSecretSource"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["client_secret_source"]
            )
        )
    out["name"] = value["name"]
    out["credentialProviderArn"] = value["credential_provider_arn"]
    if "callback_url" in value:
        out["callbackUrl"] = value["callback_url"]
    if "oauth2_provider_config_output" in value:
        import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output

        out["oauth2ProviderConfigOutput"] = (
            aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output.serialize_json(
                value["oauth2_provider_config_output"]
            )
        )
    if "status" in value:
        import aws_sdk_bedrock_agentcore_control.types.status

        out["status"] = aws_sdk_bedrock_agentcore_control.types.status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> CreateOauth2CredentialProviderResponse:
    out: CreateOauth2CredentialProviderResponse = {}  # type: ignore[typeddict-item]
    if "clientSecretArn" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret

        out["client_secret_arn"] = (
            aws_sdk_bedrock_agentcore_control.types.secret.deserialize_json(
                data["clientSecretArn"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOauth2CredentialProviderResponse.client_secret_arn required"
        )
    if "clientSecretJsonKey" in data:
        out["client_secret_json_key"] = data["clientSecretJsonKey"]
    if "clientSecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["client_secret_source"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["clientSecretSource"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateOauth2CredentialProviderResponse.name required"
        )
    if "credentialProviderArn" in data:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        raise DeserializationError(
            "CreateOauth2CredentialProviderResponse.credential_provider_arn required"
        )
    if "callbackUrl" in data:
        out["callback_url"] = data["callbackUrl"]
    if "oauth2ProviderConfigOutput" in data:
        import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output

        out["oauth2_provider_config_output"] = (
            aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output.deserialize_json(
                data["oauth2ProviderConfigOutput"]
            )
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.status

        out["status"] = aws_sdk_bedrock_agentcore_control.types.status.deserialize_json(
            data["status"]
        )
    return out
