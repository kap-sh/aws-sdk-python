"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.crypto_x402_payment_input


class _PaymentInput_cryptoX402(TypedDict):
    cryptoX402: "aws_sdk_bedrock_agentcore.types.crypto_x402_payment_input.CryptoX402PaymentInput"


PaymentInput: TypeAlias = _PaymentInput_cryptoX402


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInput) -> dict:
    if "cryptoX402" in value:
        import aws_sdk_bedrock_agentcore.types.crypto_x402_payment_input

        return {
            "cryptoX402": aws_sdk_bedrock_agentcore.types.crypto_x402_payment_input.serialize_json(
                value["cryptoX402"]
            )
        }
    else:
        raise SerializationError("PaymentInput: no variant present")


def deserialize_json(data: dict) -> PaymentInput:
    if "cryptoX402" in data:
        import aws_sdk_bedrock_agentcore.types.crypto_x402_payment_input

        return {
            "cryptoX402": aws_sdk_bedrock_agentcore.types.crypto_x402_payment_input.deserialize_json(
                data["cryptoX402"]
            )
        }
    else:
        raise DeserializationError("PaymentInput: no recognized variant key")
