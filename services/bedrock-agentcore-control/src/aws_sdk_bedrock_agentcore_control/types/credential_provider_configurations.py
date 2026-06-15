"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProviderConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_configuration

CredentialProviderConfigurations: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.credential_provider_configuration.CredentialProviderConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialProviderConfigurations) -> list:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.credential_provider_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CredentialProviderConfigurations:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_configuration

    out: CredentialProviderConfigurations = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.credential_provider_configuration.deserialize_json(
                item
            )
        )
    return out
