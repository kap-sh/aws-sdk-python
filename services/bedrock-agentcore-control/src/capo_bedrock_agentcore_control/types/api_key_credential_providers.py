"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiKeyCredentialProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_key_credential_provider_item

ApiKeyCredentialProviders: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.api_key_credential_provider_item.ApiKeyCredentialProviderItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyCredentialProviders) -> list:
    import capo_bedrock_agentcore_control.types.api_key_credential_provider_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.api_key_credential_provider_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ApiKeyCredentialProviders:
    import capo_bedrock_agentcore_control.types.api_key_credential_provider_item

    out: ApiKeyCredentialProviders = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.api_key_credential_provider_item.deserialize_json(
                item
            )
        )
    return out
