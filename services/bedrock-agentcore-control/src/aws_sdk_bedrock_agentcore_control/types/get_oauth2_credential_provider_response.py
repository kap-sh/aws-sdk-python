"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetOauth2CredentialProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_arn_type
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type
    import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output
    import aws_sdk_bedrock_agentcore_control.types.secret
    import aws_sdk_bedrock_agentcore_control.types.secret_json_key_type
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type
    import aws_sdk_bedrock_agentcore_control.types.status
    import datetime

class GetOauth2CredentialProviderResponse(TypedDict):
    client_secret_arn: "aws_sdk_bedrock_agentcore_control.types.secret.Secret"
    """<p>The Amazon Resource Name (ARN) of the client secret in AWS Secrets Manager.</p>"""
    client_secret_json_key: NotRequired["aws_sdk_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"]
    """<p>The JSON key used to extract the client secret value from the AWS Secrets Manager secret.</p>"""
    client_secret_source: NotRequired["aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"]
    """<p>The source type of the client secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in AWS Secrets Manager.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the OAuth2 credential provider.</p>"""
    credential_provider_arn: "aws_sdk_bedrock_agentcore_control.types.credential_provider_arn_type.CredentialProviderArnType"
    """<p>ARN of the credential provider requested.</p>"""
    credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType"
    """<p>The vendor of the OAuth2 credential provider.</p>"""
    callback_url: NotRequired["str"]
    """<p>Callback URL to register on the OAuth2 credential provider as an allowed callback URL. This URL is where the OAuth2 authorization server redirects users after they complete the authorization flow.</p>"""
    oauth2_provider_config_output: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output.Oauth2ProviderConfigOutput"
    """<p>The configuration output for the OAuth2 provider.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the OAuth2 credential provider was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The timestamp when the OAuth2 credential provider was last updated.</p>"""
    status: NotRequired["aws_sdk_bedrock_agentcore_control.types.status.Status"]
    """<p>The current status of the OAuth2 credential provider.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the OAuth2 credential provider is in a failed state.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetOauth2CredentialProviderResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.secret
    out["clientSecretArn"] = aws_sdk_bedrock_agentcore_control.types.secret.serialize_json(value["client_secret_arn"])
    if "client_secret_json_key" in value:
        out["clientSecretJsonKey"] = value["client_secret_json_key"]
    if "client_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type
        out["clientSecretSource"] = aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(value["client_secret_source"])
    out["name"] = value["name"]
    out["credentialProviderArn"] = value["credential_provider_arn"]
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type
    out["credentialProviderVendor"] = aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.serialize_json(value["credential_provider_vendor"])
    if "callback_url" in value:
        out["callbackUrl"] = value["callback_url"]
    import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output
    out["oauth2ProviderConfigOutput"] = aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output.serialize_json(value["oauth2_provider_config_output"])
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
    out["createdTime"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(value["created_time"])
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
    out["lastUpdatedTime"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(value["last_updated_time"])
    if "status" in value:
        import aws_sdk_bedrock_agentcore_control.types.status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.status.serialize_json(value["status"])
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> GetOauth2CredentialProviderResponse:
    out: GetOauth2CredentialProviderResponse = {}  # type: ignore[typeddict-item]
    if "clientSecretArn" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret
        out["client_secret_arn"] = aws_sdk_bedrock_agentcore_control.types.secret.deserialize_json(data["clientSecretArn"])
    else:
        raise DeserializationError("GetOauth2CredentialProviderResponse.client_secret_arn required")
    if "clientSecretJsonKey" in data:
        out["client_secret_json_key"] = data["clientSecretJsonKey"]
    if "clientSecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type
        out["client_secret_source"] = aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(data["clientSecretSource"])
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetOauth2CredentialProviderResponse.name required")
    if "credentialProviderArn" in data:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        raise DeserializationError("GetOauth2CredentialProviderResponse.credential_provider_arn required")
    if "credentialProviderVendor" in data:
        import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type
        out["credential_provider_vendor"] = aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.deserialize_json(data["credentialProviderVendor"])
    else:
        raise DeserializationError("GetOauth2CredentialProviderResponse.credential_provider_vendor required")
    if "callbackUrl" in data:
        out["callback_url"] = data["callbackUrl"]
    if "oauth2ProviderConfigOutput" in data:
        import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output
        out["oauth2_provider_config_output"] = aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_output.deserialize_json(data["oauth2ProviderConfigOutput"])
    else:
        raise DeserializationError("GetOauth2CredentialProviderResponse.oauth2_provider_config_output required")
    if "createdTime" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
        out["created_time"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(data["createdTime"])
    else:
        raise DeserializationError("GetOauth2CredentialProviderResponse.created_time required")
    if "lastUpdatedTime" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
        out["last_updated_time"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(data["lastUpdatedTime"])
    else:
        raise DeserializationError("GetOauth2CredentialProviderResponse.last_updated_time required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.status.deserialize_json(data["status"])
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out