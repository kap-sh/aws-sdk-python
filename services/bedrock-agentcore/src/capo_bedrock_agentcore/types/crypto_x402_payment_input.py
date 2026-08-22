"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CryptoX402PaymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_document


class CryptoX402PaymentInput(TypedDict, closed=True):
    version: "str"
    """<p>The version of the X402 protocol.</p>"""
    payload: "capo_bedrock_agentcore.types.payment_document.PaymentDocument"
    """<p>The X402 payment payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CryptoX402PaymentInput) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    out["payload"] = value["payload"]
    return out


def deserialize_json(data: dict) -> CryptoX402PaymentInput:
    out: CryptoX402PaymentInput = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CryptoX402PaymentInput.version required")
    if data.get("payload") is not None:
        out["payload"] = data["payload"]
    else:
        raise DeserializationError("CryptoX402PaymentInput.payload required")
    return out
