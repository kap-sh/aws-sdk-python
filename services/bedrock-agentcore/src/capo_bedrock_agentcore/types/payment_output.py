"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.crypto_x402_payment_output


class _PaymentOutput_cryptoX402(TypedDict, closed=True):
    cryptoX402: "capo_bedrock_agentcore.types.crypto_x402_payment_output.CryptoX402PaymentOutput"


PaymentOutput: TypeAlias = _PaymentOutput_cryptoX402


# --- restJson1 ser/de ---
def serialize_json(value: PaymentOutput) -> dict:
    if "cryptoX402" in value:
        import capo_bedrock_agentcore.types.crypto_x402_payment_output

        return {
            "cryptoX402": capo_bedrock_agentcore.types.crypto_x402_payment_output.serialize_json(
                value["cryptoX402"]
            )
        }
    else:
        raise SerializationError("PaymentOutput: no variant present")


def deserialize_json(data: dict) -> PaymentOutput:
    if data.get("cryptoX402") is not None:
        import capo_bedrock_agentcore.types.crypto_x402_payment_output

        return {
            "cryptoX402": capo_bedrock_agentcore.types.crypto_x402_payment_output.deserialize_json(
                data["cryptoX402"]
            )
        }
    else:
        raise DeserializationError("PaymentOutput: no recognized variant key")
