"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.crypto_x402_payment_input


class _PaymentInput_cryptoX402(TypedDict, closed=True):
    cryptoX402: (
        "capo_bedrock_agentcore.types.crypto_x402_payment_input.CryptoX402PaymentInput"
    )


PaymentInput: TypeAlias = _PaymentInput_cryptoX402


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInput) -> dict:
    if "cryptoX402" in value:
        import capo_bedrock_agentcore.types.crypto_x402_payment_input

        return {
            "cryptoX402": capo_bedrock_agentcore.types.crypto_x402_payment_input.serialize_json(
                value["cryptoX402"]
            )
        }
    else:
        raise SerializationError("PaymentInput: no variant present")


def deserialize_json(data: dict) -> PaymentInput:
    if data.get("cryptoX402") is not None:
        import capo_bedrock_agentcore.types.crypto_x402_payment_input

        return {
            "cryptoX402": capo_bedrock_agentcore.types.crypto_x402_payment_input.deserialize_json(
                data["cryptoX402"]
            )
        }
    else:
        raise DeserializationError("PaymentInput: no recognized variant key")
