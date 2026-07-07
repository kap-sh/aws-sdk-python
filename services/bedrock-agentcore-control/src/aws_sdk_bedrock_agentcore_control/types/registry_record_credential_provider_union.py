"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordCredentialProviderUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.registry_record_iam_credential_provider
    import aws_sdk_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider


class _RegistryRecordCredentialProviderUnion_oauthCredentialProvider(
    TypedDict, closed=True
):
    oauthCredentialProvider: "aws_sdk_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider.RegistryRecordOAuthCredentialProvider"


class _RegistryRecordCredentialProviderUnion_iamCredentialProvider(
    TypedDict, closed=True
):
    iamCredentialProvider: "aws_sdk_bedrock_agentcore_control.types.registry_record_iam_credential_provider.RegistryRecordIamCredentialProvider"


RegistryRecordCredentialProviderUnion: TypeAlias = (
    _RegistryRecordCredentialProviderUnion_oauthCredentialProvider
    | _RegistryRecordCredentialProviderUnion_iamCredentialProvider
)


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordCredentialProviderUnion) -> dict:
    if "oauthCredentialProvider" in value:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider

        return {
            "oauthCredentialProvider": aws_sdk_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider.serialize_json(
                value["oauthCredentialProvider"]
            )
        }
    elif "iamCredentialProvider" in value:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_iam_credential_provider

        return {
            "iamCredentialProvider": aws_sdk_bedrock_agentcore_control.types.registry_record_iam_credential_provider.serialize_json(
                value["iamCredentialProvider"]
            )
        }
    else:
        raise SerializationError(
            "RegistryRecordCredentialProviderUnion: no variant present"
        )


def deserialize_json(data: dict) -> RegistryRecordCredentialProviderUnion:
    if "oauthCredentialProvider" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider

        return {
            "oauthCredentialProvider": aws_sdk_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider.deserialize_json(
                data["oauthCredentialProvider"]
            )
        }
    elif "iamCredentialProvider" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_iam_credential_provider

        return {
            "iamCredentialProvider": aws_sdk_bedrock_agentcore_control.types.registry_record_iam_credential_provider.deserialize_json(
                data["iamCredentialProvider"]
            )
        }
    else:
        raise DeserializationError(
            "RegistryRecordCredentialProviderUnion: no recognized variant key"
        )
