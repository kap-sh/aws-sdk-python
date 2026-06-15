"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProviderConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_type


class CredentialProviderConfiguration(TypedDict):
    credential_provider_type: "aws_sdk_bedrock_agentcore_control.types.credential_provider_type.CredentialProviderType"
    """<p>The type of credential provider. This field specifies which authentication method the gateway uses.</p>"""
    credential_provider: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.credential_provider.CredentialProvider"
    ]
    """<p>The credential provider. This field contains the specific configuration for the credential provider type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CredentialProviderConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_type

    out["credentialProviderType"] = (
        aws_sdk_bedrock_agentcore_control.types.credential_provider_type.serialize_json(
            value["credential_provider_type"]
        )
    )
    if "credential_provider" in value:
        import aws_sdk_bedrock_agentcore_control.types.credential_provider

        out["credentialProvider"] = (
            aws_sdk_bedrock_agentcore_control.types.credential_provider.serialize_json(
                value["credential_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> CredentialProviderConfiguration:
    out: CredentialProviderConfiguration = {}  # type: ignore[typeddict-item]
    if "credentialProviderType" in data:
        import aws_sdk_bedrock_agentcore_control.types.credential_provider_type

        out["credential_provider_type"] = (
            aws_sdk_bedrock_agentcore_control.types.credential_provider_type.deserialize_json(
                data["credentialProviderType"]
            )
        )
    else:
        raise DeserializationError(
            "CredentialProviderConfiguration.credential_provider_type required"
        )
    if "credentialProvider" in data:
        import aws_sdk_bedrock_agentcore_control.types.credential_provider

        out["credential_provider"] = (
            aws_sdk_bedrock_agentcore_control.types.credential_provider.deserialize_json(
                data["credentialProvider"]
            )
        )
    return out
