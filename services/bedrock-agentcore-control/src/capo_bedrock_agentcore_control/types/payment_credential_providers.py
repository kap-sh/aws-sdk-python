"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentCredentialProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.payment_credential_provider_item

PaymentCredentialProviders: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.payment_credential_provider_item.PaymentCredentialProviderItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentCredentialProviders) -> list:
    import capo_bedrock_agentcore_control.types.payment_credential_provider_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.payment_credential_provider_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PaymentCredentialProviders:
    import capo_bedrock_agentcore_control.types.payment_credential_provider_item

    out: PaymentCredentialProviders = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.payment_credential_provider_item.deserialize_json(
                item
            )
        )
    return out
