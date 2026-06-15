"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentTokenResponseOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_response_output
    import aws_sdk_bedrock_agentcore.types.stripe_privy_token_response_output


class _PaymentTokenResponseOutput_coinbaseCdpTokenResponse(TypedDict):
    coinbaseCdpTokenResponse: "aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_response_output.CoinbaseCdpTokenResponseOutput"


class _PaymentTokenResponseOutput_stripePrivyTokenResponse(TypedDict):
    stripePrivyTokenResponse: "aws_sdk_bedrock_agentcore.types.stripe_privy_token_response_output.StripePrivyTokenResponseOutput"


PaymentTokenResponseOutput: TypeAlias = (
    _PaymentTokenResponseOutput_coinbaseCdpTokenResponse
    | _PaymentTokenResponseOutput_stripePrivyTokenResponse
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentTokenResponseOutput) -> dict:
    if "coinbaseCdpTokenResponse" in value:
        import aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_response_output

        return {
            "coinbaseCdpTokenResponse": aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_response_output.serialize_json(
                value["coinbaseCdpTokenResponse"]
            )
        }
    elif "stripePrivyTokenResponse" in value:
        import aws_sdk_bedrock_agentcore.types.stripe_privy_token_response_output

        return {
            "stripePrivyTokenResponse": aws_sdk_bedrock_agentcore.types.stripe_privy_token_response_output.serialize_json(
                value["stripePrivyTokenResponse"]
            )
        }
    else:
        raise SerializationError("PaymentTokenResponseOutput: no variant present")


def deserialize_json(data: dict) -> PaymentTokenResponseOutput:
    if "coinbaseCdpTokenResponse" in data:
        import aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_response_output

        return {
            "coinbaseCdpTokenResponse": aws_sdk_bedrock_agentcore.types.coinbase_cdp_token_response_output.deserialize_json(
                data["coinbaseCdpTokenResponse"]
            )
        }
    elif "stripePrivyTokenResponse" in data:
        import aws_sdk_bedrock_agentcore.types.stripe_privy_token_response_output

        return {
            "stripePrivyTokenResponse": aws_sdk_bedrock_agentcore.types.stripe_privy_token_response_output.deserialize_json(
                data["stripePrivyTokenResponse"]
            )
        }
    else:
        raise DeserializationError(
            "PaymentTokenResponseOutput: no recognized variant key"
        )
