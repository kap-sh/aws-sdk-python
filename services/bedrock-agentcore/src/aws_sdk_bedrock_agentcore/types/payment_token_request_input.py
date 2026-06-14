"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentTokenRequestInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_request_input
    import aws_sdk_bedrock_agentcore.types.stripe_privy_token_request_input


class _PaymentTokenRequestInput_coinbaseCdpTokenRequest(TypedDict):
    coinbaseCdpTokenRequest: "aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_request_input.CoinbaseCdpTokenRequestInput"


class _PaymentTokenRequestInput_stripePrivyTokenRequest(TypedDict):
    stripePrivyTokenRequest: "aws_sdk_bedrock_agentcore.types.stripe_privy_token_request_input.StripePrivyTokenRequestInput"


PaymentTokenRequestInput: TypeAlias = (
    _PaymentTokenRequestInput_coinbaseCdpTokenRequest
    | _PaymentTokenRequestInput_stripePrivyTokenRequest
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentTokenRequestInput) -> dict:
    if "coinbaseCdpTokenRequest" in value:
        import aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_request_input

        return {
            "coinbaseCdpTokenRequest": aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_request_input.serialize_json(
                value["coinbaseCdpTokenRequest"]
            )
        }
    elif "stripePrivyTokenRequest" in value:
        import aws_sdk_bedrock_agentcore.types.stripe_privy_token_request_input

        return {
            "stripePrivyTokenRequest": aws_sdk_bedrock_agentcore.types.stripe_privy_token_request_input.serialize_json(
                value["stripePrivyTokenRequest"]
            )
        }
    else:
        raise SerializationError("PaymentTokenRequestInput: no variant present")


def deserialize_json(data: dict) -> PaymentTokenRequestInput:
    if "coinbaseCdpTokenRequest" in data:
        import aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_request_input

        return {
            "coinbaseCdpTokenRequest": aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_request_input.deserialize_json(
                data["coinbaseCdpTokenRequest"]
            )
        }
    elif "stripePrivyTokenRequest" in data:
        import aws_sdk_bedrock_agentcore.types.stripe_privy_token_request_input

        return {
            "stripePrivyTokenRequest": aws_sdk_bedrock_agentcore.types.stripe_privy_token_request_input.deserialize_json(
                data["stripePrivyTokenRequest"]
            )
        }
    else:
        raise DeserializationError(
            "PaymentTokenRequestInput: no recognized variant key"
        )
