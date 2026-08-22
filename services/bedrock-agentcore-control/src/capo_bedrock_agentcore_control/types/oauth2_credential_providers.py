"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Oauth2CredentialProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.oauth2_credential_provider_item

Oauth2CredentialProviders: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.oauth2_credential_provider_item.Oauth2CredentialProviderItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2CredentialProviders) -> list:
    import capo_bedrock_agentcore_control.types.oauth2_credential_provider_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.oauth2_credential_provider_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> Oauth2CredentialProviders:
    import capo_bedrock_agentcore_control.types.oauth2_credential_provider_item

    out: Oauth2CredentialProviders = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.oauth2_credential_provider_item.deserialize_json(
                item
            )
        )
    return out
