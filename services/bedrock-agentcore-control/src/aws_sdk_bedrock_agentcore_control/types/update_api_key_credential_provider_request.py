"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateApiKeyCredentialProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.default_api_key_type
    import aws_sdk_bedrock_agentcore_control.types.secret_reference
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type


class UpdateApiKeyCredentialProviderRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the API key credential provider to update.</p>"""
    api_key: (
        "aws_sdk_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
    )
    """<p>The new API key to use for authentication. This value replaces the existing API key and is encrypted and stored securely.</p>"""
    api_key_secret_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the AWS Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    api_key_secret_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApiKeyCredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["apiKey"] = value.get("api_key", "")
    if "api_key_secret_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference

        out["apiKeySecretConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["api_key_secret_config"]
            )
        )
    if "api_key_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["apiKeySecretSource"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["api_key_secret_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApiKeyCredentialProviderRequest:
    out: UpdateApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "UpdateApiKeyCredentialProviderRequest.name required"
        )
    if "apiKey" in data:
        out["api_key"] = data["apiKey"]
    else:
        out["api_key"] = ""
    if "apiKeySecretConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference

        out["api_key_secret_config"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["apiKeySecretConfig"]
            )
        )
    if "apiKeySecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["api_key_secret_source"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["apiKeySecretSource"]
            )
        )
    return out
