"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentProviderConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_input


class _PaymentProviderConfigurationInput_coinbaseCdpConfiguration(TypedDict):
    coinbaseCdpConfiguration: "aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_input.CoinbaseCdpConfigurationInput"


class _PaymentProviderConfigurationInput_stripePrivyConfiguration(TypedDict):
    stripePrivyConfiguration: "aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_input.StripePrivyConfigurationInput"


PaymentProviderConfigurationInput: TypeAlias = (
    _PaymentProviderConfigurationInput_coinbaseCdpConfiguration
    | _PaymentProviderConfigurationInput_stripePrivyConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentProviderConfigurationInput) -> dict:
    if "coinbaseCdpConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_input

        return {
            "coinbaseCdpConfiguration": aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_input.serialize_json(
                value["coinbaseCdpConfiguration"]
            )
        }
    elif "stripePrivyConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_input

        return {
            "stripePrivyConfiguration": aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_input.serialize_json(
                value["stripePrivyConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "PaymentProviderConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> PaymentProviderConfigurationInput:
    if "coinbaseCdpConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_input

        return {
            "coinbaseCdpConfiguration": aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_input.deserialize_json(
                data["coinbaseCdpConfiguration"]
            )
        }
    elif "stripePrivyConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_input

        return {
            "stripePrivyConfiguration": aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_input.deserialize_json(
                data["stripePrivyConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "PaymentProviderConfigurationInput: no recognized variant key"
        )
