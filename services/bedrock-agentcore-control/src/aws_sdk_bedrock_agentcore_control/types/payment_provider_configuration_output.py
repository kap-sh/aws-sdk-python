"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentProviderConfigurationOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_output
    import aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_output


class _PaymentProviderConfigurationOutput_coinbaseCdpConfiguration(TypedDict):
    coinbaseCdpConfiguration: "aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_output.CoinbaseCdpConfigurationOutput"


class _PaymentProviderConfigurationOutput_stripePrivyConfiguration(TypedDict):
    stripePrivyConfiguration: "aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_output.StripePrivyConfigurationOutput"


PaymentProviderConfigurationOutput: TypeAlias = (
    _PaymentProviderConfigurationOutput_coinbaseCdpConfiguration
    | _PaymentProviderConfigurationOutput_stripePrivyConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentProviderConfigurationOutput) -> dict:
    if "coinbaseCdpConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_output

        return {
            "coinbaseCdpConfiguration": aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_output.serialize_json(
                value["coinbaseCdpConfiguration"]
            )
        }
    elif "stripePrivyConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_output

        return {
            "stripePrivyConfiguration": aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_output.serialize_json(
                value["stripePrivyConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "PaymentProviderConfigurationOutput: no variant present"
        )


def deserialize_json(data: dict) -> PaymentProviderConfigurationOutput:
    if "coinbaseCdpConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_output

        return {
            "coinbaseCdpConfiguration": aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_configuration_output.deserialize_json(
                data["coinbaseCdpConfiguration"]
            )
        }
    elif "stripePrivyConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_output

        return {
            "stripePrivyConfiguration": aws_sdk_bedrock_agentcore_control.types.stripe_privy_configuration_output.deserialize_json(
                data["stripePrivyConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "PaymentProviderConfigurationOutput: no recognized variant key"
        )
