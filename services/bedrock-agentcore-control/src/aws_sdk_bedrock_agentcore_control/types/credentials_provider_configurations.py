"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialsProviderConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credentials_provider_configuration

CredentialsProviderConfigurations: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.credentials_provider_configuration.CredentialsProviderConfiguration"]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialsProviderConfigurations) -> list:
    import aws_sdk_bedrock_agentcore_control.types.credentials_provider_configuration
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.credentials_provider_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> CredentialsProviderConfigurations:
    import aws_sdk_bedrock_agentcore_control.types.credentials_provider_configuration
    out: CredentialsProviderConfigurations = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore_control.types.credentials_provider_configuration.deserialize_json(item))
    return out