"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CryptoX402PaymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_document


class CryptoX402PaymentOutput(TypedDict, closed=True):
    version: "str"
    """<p>The version of the X402 protocol.</p>"""
    payload: "capo_bedrock_agentcore.types.payment_document.PaymentDocument"
    """<p>The X402 payment response payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CryptoX402PaymentOutput) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    out["payload"] = value["payload"]
    return out


def deserialize_json(data: dict) -> CryptoX402PaymentOutput:
    out: CryptoX402PaymentOutput = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CryptoX402PaymentOutput.version required")
    if "payload" in data:
        out["payload"] = data["payload"]
    else:
        raise DeserializationError("CryptoX402PaymentOutput.payload required")
    return out
