"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateApiKeyCredentialProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.api_key_credential_provider_arn_type
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.secret
    import aws_sdk_bedrock_agentcore_control.types.secret_json_key_type
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type

class CreateApiKeyCredentialProviderResponse(TypedDict):
    api_key_secret_arn: "aws_sdk_bedrock_agentcore_control.types.secret.Secret"
    """<p>The Amazon Resource Name (ARN) of the secret containing the API key.</p>"""
    api_key_secret_json_key: NotRequired["aws_sdk_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"]
    """<p>The JSON key used to extract the API key value from the AWS Secrets Manager secret.</p>"""
    api_key_secret_source: NotRequired["aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"]
    """<p>The source type of the API key secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in AWS Secrets Manager.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the created API key credential provider.</p>"""
    credential_provider_arn: "aws_sdk_bedrock_agentcore_control.types.api_key_credential_provider_arn_type.ApiKeyCredentialProviderArnType"
    """<p>The Amazon Resource Name (ARN) of the created API key credential provider.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateApiKeyCredentialProviderResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.secret
    out["apiKeySecretArn"] = aws_sdk_bedrock_agentcore_control.types.secret.serialize_json(value["api_key_secret_arn"])
    if "api_key_secret_json_key" in value:
        out["apiKeySecretJsonKey"] = value["api_key_secret_json_key"]
    if "api_key_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type
        out["apiKeySecretSource"] = aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(value["api_key_secret_source"])
    out["name"] = value["name"]
    out["credentialProviderArn"] = value["credential_provider_arn"]
    return out


def deserialize_json(data: dict) -> CreateApiKeyCredentialProviderResponse:
    out: CreateApiKeyCredentialProviderResponse = {}  # type: ignore[typeddict-item]
    if "apiKeySecretArn" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret
        out["api_key_secret_arn"] = aws_sdk_bedrock_agentcore_control.types.secret.deserialize_json(data["apiKeySecretArn"])
    else:
        raise DeserializationError("CreateApiKeyCredentialProviderResponse.api_key_secret_arn required")
    if "apiKeySecretJsonKey" in data:
        out["api_key_secret_json_key"] = data["apiKeySecretJsonKey"]
    if "apiKeySecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type
        out["api_key_secret_source"] = aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(data["apiKeySecretSource"])
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateApiKeyCredentialProviderResponse.name required")
    if "credentialProviderArn" in data:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        raise DeserializationError("CreateApiKeyCredentialProviderResponse.credential_provider_arn required")
    return out