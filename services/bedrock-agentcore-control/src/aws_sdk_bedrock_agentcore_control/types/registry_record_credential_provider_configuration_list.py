"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordCredentialProviderConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_configuration

RegistryRecordCredentialProviderConfigurationList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_configuration.RegistryRecordCredentialProviderConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordCredentialProviderConfigurationList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RegistryRecordCredentialProviderConfigurationList:
    import aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_configuration

    out: RegistryRecordCredentialProviderConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.registry_record_credential_provider_configuration.deserialize_json(
                item
            )
        )
    return out
