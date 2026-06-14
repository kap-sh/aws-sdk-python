"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordCredentialProviderConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_type
    import aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_union


class RegistryRecordCredentialProviderConfiguration(TypedDict):
    credential_provider_type: "aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_type.RegistryRecordCredentialProviderType"
    """<p>The type of credential provider.</p> <ul> <li> <p> <code>OAUTH</code> - OAuth-based authentication.</p> </li> <li> <p> <code>IAM</code> - Amazon Web Services IAM-based authentication using SigV4 signing.</p> </li> </ul>"""
    credential_provider: "aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_union.RegistryRecordCredentialProviderUnion"
    """<p>The credential provider configuration details. The structure depends on the <code>credentialProviderType</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordCredentialProviderConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_type

    out["credentialProviderType"] = (
        aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_type.serialize_json(
            value["credential_provider_type"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_union

    out["credentialProvider"] = (
        aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_union.serialize_json(
            value["credential_provider"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegistryRecordCredentialProviderConfiguration:
    out: RegistryRecordCredentialProviderConfiguration = {}  # type: ignore[typeddict-item]
    if "credentialProviderType" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_type

        out["credential_provider_type"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_type.deserialize_json(
                data["credentialProviderType"]
            )
        )
    else:
        raise DeserializationError(
            "RegistryRecordCredentialProviderConfiguration.credential_provider_type required"
        )
    if "credentialProvider" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_union

        out["credential_provider"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_union.deserialize_json(
                data["credentialProvider"]
            )
        )
    else:
        raise DeserializationError(
            "RegistryRecordCredentialProviderConfiguration.credential_provider required"
        )
    return out
