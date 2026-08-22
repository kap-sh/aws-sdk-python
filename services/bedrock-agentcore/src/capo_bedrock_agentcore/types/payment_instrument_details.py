"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInstrumentDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.embedded_crypto_wallet


class _PaymentInstrumentDetails_embeddedCryptoWallet(TypedDict, closed=True):
    embeddedCryptoWallet: (
        "capo_bedrock_agentcore.types.embedded_crypto_wallet.EmbeddedCryptoWallet"
    )


PaymentInstrumentDetails: TypeAlias = _PaymentInstrumentDetails_embeddedCryptoWallet


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInstrumentDetails) -> dict:
    if "embeddedCryptoWallet" in value:
        import capo_bedrock_agentcore.types.embedded_crypto_wallet

        return {
            "embeddedCryptoWallet": capo_bedrock_agentcore.types.embedded_crypto_wallet.serialize_json(
                value["embeddedCryptoWallet"]
            )
        }
    else:
        raise SerializationError("PaymentInstrumentDetails: no variant present")


def deserialize_json(data: dict) -> PaymentInstrumentDetails:
    if data.get("embeddedCryptoWallet") is not None:
        import capo_bedrock_agentcore.types.embedded_crypto_wallet

        return {
            "embeddedCryptoWallet": capo_bedrock_agentcore.types.embedded_crypto_wallet.deserialize_json(
                data["embeddedCryptoWallet"]
            )
        }
    else:
        raise DeserializationError(
            "PaymentInstrumentDetails: no recognized variant key"
        )
