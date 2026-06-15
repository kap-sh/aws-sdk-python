"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateOauth2CredentialProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type
    import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input


class UpdateOauth2CredentialProviderRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the OAuth2 credential provider to update.</p>"""
    credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType"
    """<p>The vendor of the OAuth2 credential provider.</p>"""
    oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput"
    """<p>The configuration input for the OAuth2 provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOauth2CredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type

    out["credentialProviderVendor"] = (
        aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.serialize_json(
            value["credential_provider_vendor"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input

    out["oauth2ProviderConfigInput"] = (
        aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.serialize_json(
            value["oauth2_provider_config_input"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateOauth2CredentialProviderRequest:
    out: UpdateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "UpdateOauth2CredentialProviderRequest.name required"
        )
    if "credentialProviderVendor" in data:
        import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type

        out["credential_provider_vendor"] = (
            aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.deserialize_json(
                data["credentialProviderVendor"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateOauth2CredentialProviderRequest.credential_provider_vendor required"
        )
    if "oauth2ProviderConfigInput" in data:
        import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input

        out["oauth2_provider_config_input"] = (
            aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.deserialize_json(
                data["oauth2ProviderConfigInput"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateOauth2CredentialProviderRequest.oauth2_provider_config_input required"
        )
    return out
