"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Oauth2CredentialProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.oauth2_credential_provider_item

Oauth2CredentialProviders: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.oauth2_credential_provider_item.Oauth2CredentialProviderItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2CredentialProviders) -> list:
    import aws_sdk_bedrock_agentcore_control.types.oauth2_credential_provider_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.oauth2_credential_provider_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> Oauth2CredentialProviders:
    import aws_sdk_bedrock_agentcore_control.types.oauth2_credential_provider_item

    out: Oauth2CredentialProviders = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.oauth2_credential_provider_item.deserialize_json(
                item
            )
        )
    return out
