"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateOauth2CredentialProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type
    import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input
    import aws_sdk_bedrock_agentcore_control.types.tags_map

class CreateOauth2CredentialProviderRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the OAuth2 credential provider. The name must be unique within your account.</p>"""
    credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType"
    """<p>The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.</p>"""
    oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput"
    """<p>The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateOauth2CredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type
    out["credentialProviderVendor"] = aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.serialize_json(value["credential_provider_vendor"])
    import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input
    out["oauth2ProviderConfigInput"] = aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.serialize_json(value["oauth2_provider_config_input"])
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateOauth2CredentialProviderRequest:
    out: CreateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateOauth2CredentialProviderRequest.name required")
    if "credentialProviderVendor" in data:
        import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type
        out["credential_provider_vendor"] = aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.deserialize_json(data["credentialProviderVendor"])
    else:
        raise DeserializationError("CreateOauth2CredentialProviderRequest.credential_provider_vendor required")
    if "oauth2ProviderConfigInput" in data:
        import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input
        out["oauth2_provider_config_input"] = aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.deserialize_json(data["oauth2ProviderConfigInput"])
    else:
        raise DeserializationError("CreateOauth2CredentialProviderRequest.oauth2_provider_config_input required")
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(data["tags"])
    return out