"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialsProviderConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credentials_provider_configuration

CredentialsProviderConfigurations: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.credentials_provider_configuration.CredentialsProviderConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialsProviderConfigurations) -> list:
    import capo_bedrock_agentcore_control.types.credentials_provider_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.credentials_provider_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CredentialsProviderConfigurations:
    import capo_bedrock_agentcore_control.types.credentials_provider_configuration

    out: CredentialsProviderConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.credentials_provider_configuration.deserialize_json(
                item
            )
        )
    return out
